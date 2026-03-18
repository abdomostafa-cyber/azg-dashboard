import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
import plotly.io as pio

pio.renderers.default = "browser"

# Load data
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE = os.path.join(BASE_DIR, "data/azg_vs_gold_egp.xlsx")

df = pd.read_excel(FILE)
df["date"] = pd.to_datetime(df["date"])

# -----------------------
# PREP DATA
# -----------------------
df = df.sort_values("date")

# Create indices (base = 100)
df["azg_index"] = df["azg_nav"] / df["azg_nav"].iloc[0] * 100
df["gold_index"] = df["gold_egp_per_gram"] / df["gold_egp_per_gram"].iloc[0] * 100

# -----------------------
# CREATE SUBPLOTS
# -----------------------
fig = make_subplots(
    rows=3, cols=1,
    shared_xaxes=True,
    vertical_spacing=0.05,
    subplot_titles=(
        "AZG NAV vs Gold (EGP) — Log Scale",
        "Indexed Performance (Base = 100)",
        "Tracking Difference"
    )
)

# -----------------------
# TOP: LOG SCALE LEVELS
# -----------------------
fig.add_trace(
    go.Scatter(x=df["date"], y=df["gold_egp_per_gram"],
               name="Gold (EGP/g)", line=dict(width=2)),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=df["date"], y=df["azg_nav"],
               name="AZG NAV", line=dict(width=2)),
    row=1, col=1
)

# Apply log scale
fig.update_yaxes(type="log", row=1, col=1)

# -----------------------
# MIDDLE: INDEXED PERFORMANCE
# -----------------------
fig.add_trace(
    go.Scatter(x=df["date"], y=df["gold_index"],
               name="Gold Index", line=dict(width=2)),
    row=2, col=1
)

fig.add_trace(
    go.Scatter(x=df["date"], y=df["azg_index"],
               name="AZG Index", line=dict(width=2)),
    row=2, col=1
)

# -----------------------
# BOTTOM: TRACKING DIFFERENCE
# -----------------------
fig.add_trace(
    go.Scatter(x=df["date"], y=df["tracking_diff"],
               name="Tracking Diff",
               line=dict(dash="dot")),
    row=3, col=1
)

# -----------------------
# LAYOUT
# -----------------------
fig.update_layout(
    title="AZG vs Gold (EGP) — Full Performance Dashboard",
    hovermode="x unified",
    height=900
)

# -----------------------
# OUTPUT
# -----------------------

write_path = os.path.join(BASE_DIR, "outputs/dashboard.html")
fig.write_html(write_path, auto_open=True)