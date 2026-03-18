
# AZG Gold Fund Tracking Analysis

This project analyzes how the AZG gold fund tracks the underlying price of gold in Egyptian Pounds (EGP), using publicly available data.

## 🔗 Live Dashboard
Interactive visualization:
[Link to dashboard](https://abdomostafa-cyber.github.io/azg-dashboard/)

---

## 📊 Key Findings

- Gold (EGP per gram) increased by ~332% over the analysis period  
- AZG NAV increased by ~180% over the same period  
- AZG captured only ~54% of the underlying gold return  
- The cumulative performance gap reached ~160 percentage points  

The data shows:
- An initial period of slight overperformance  
- Followed by persistent and widening underperformance  

This suggests a structural tracking deviation rather than short-term noise.

---

## 🧠 Methodology

### 1. Data Sources
- AZG NAV data (Azimut API / Mubasher)
- Gold price (XAU/USD)
- USD/EGP exchange rate

### 2. Benchmark Construction

Gold benchmark was constructed as:

Gold (EGP per gram) = (Gold USD per ounce / 31.1035) × USD/EGP

This reflects the true local price of gold in Egypt.

### 3. Analysis

- Time series aligned by date  
- Prices normalized to index = 100  
- Tracking difference computed as:
  
  Tracking Difference = AZG Index – Gold Index

---

## 📈 Dashboard Components

The dashboard includes:

1. **Log-scale price comparison**
   - AZG NAV vs Gold (EGP per gram)

2. **Indexed performance (base = 100)**
   - Direct comparison of cumulative returns

3. **Tracking difference**
   - Visualizes divergence over time

---

## 📁 Repository Structure

```
├── index.html # Interactive dashboard (GitHub Pages)
├── README.md

├── data/
│ └── azg_vs_gold_egp.xlsx

├── scripts/
│ ├── fetch_data.py
│ └── dashboard.py

├── outputs/
│ └── dashboard.html
```

---

## ⚙️ Reproducibility

The full pipeline is included:

1. Fetch AZG NAV data  
2. Fetch gold and FX data  
3. Construct EGP gold benchmark  
4. Generate dataset  
5. Build dashboard  

---

## 📌 Notes

- This analysis uses publicly available data  
- FX-adjusted gold price is used as the benchmark  
- Results are sensitive to data alignment and frequency  

---

## 🤝 Contact

If you have questions or would like access to the dataset or scripts, feel free to reach out.
