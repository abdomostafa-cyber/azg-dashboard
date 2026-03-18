import requests
import pandas as pd
from datetime import datetime, UTC
import os

AZG_URL = "https://api.azimut.eg/api/list/funds/az-gold-2"
GOLD_URL = "https://stooq.com/q/d/l/?s=xauusd&i=d"
FX_URL = "https://stooq.com/q/d/l/?s=usdegp&i=d"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE = os.path.join(BASE_DIR, "data/azg_vs_gold_egp.xlsx")

# -----------------------
# AZG
# -----------------------
def fetch_azg():
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Referer": "https://azimut.eg/",
        "Origin": "https://azimut.eg"
    }

    r = requests.get(AZG_URL, headers=headers)
    r.raise_for_status()

    graph = r.json()["data"]["graph"]

    rows = []
    for ts, price in graph:
        dt = pd.to_datetime(ts, unit="ms")
        rows.append([dt, price])

    return pd.DataFrame(rows, columns=["date", "azg_nav"])


# -----------------------
# GOLD USD
# -----------------------
def fetch_gold():
    df = pd.read_csv(GOLD_URL)
    df["Date"] = pd.to_datetime(df["Date"])

    df = df.rename(columns={
        "Date": "date",
        "Close": "gold_usd"
    })

    return df[["date", "gold_usd"]]


# -----------------------
# USD/EGP
# -----------------------
def fetch_fx():
    df = pd.read_csv(FX_URL)
    df["Date"] = pd.to_datetime(df["Date"])

    df = df.rename(columns={
        "Date": "date",
        "Close": "usd_egp"
    })

    return df[["date", "usd_egp"]]


# -----------------------
# MERGE + CALCULATE
# -----------------------
def build_dataset(azg, gold, fx):

    df = azg.merge(gold, on="date", how="inner")
    df = df.merge(fx, on="date", how="inner")

    # Convert gold to EGP
    df["gold_egp_per_gram"] = (df["gold_usd"] / 31.1035) * df["usd_egp"]

    # Normalize to index = 100
    df = df.sort_values("date")

    df["azg_index"] = df["azg_nav"] / df["azg_nav"].iloc[0] * 100
    df["gold_index"] = df["gold_egp_per_gram"] / df["gold_egp_per_gram"].iloc[0] * 100

    # Tracking difference
    df["tracking_diff"] = df["azg_index"] - df["gold_index"]

    return df


# -----------------------
# MAIN
# -----------------------
def main():
    azg = fetch_azg()
    gold = fetch_gold()
    fx = fetch_fx()

    df = build_dataset(azg, gold, fx)

    df.to_excel(FILE, index=False)

    print(f"Saved to {FILE}")
    print(df.head())


if __name__ == "__main__":
    main()