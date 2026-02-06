# 🇪🇹 Ethiopia Financial Inclusion Forecast (2011–2027)

**Evidence-based forecasting and interactive analytics for financial inclusion in Ethiopia**

Built with **Python • Pandas • NumPy • Scikit-learn • Streamlit • Plotly**

---

## 🎯 Project Overview & Impact

### The Challenge
Ethiopia is experiencing a critical disconnect between **financial service supply and demand**.

Despite massive mobile money expansion:

- **65+ million mobile money accounts registered since 2021**
- **Only 49% of adults report having a financial account (2024)**
- Growth slowed to **+3pp (2021–2024)** vs **+11pp (2017–2021)**

This **73% deceleration** reveals a fundamental gap:

> **Registered accounts ≠ active users**

Policymakers, regulators, and operators need **evidence-based insights** to understand:
- What actually drives financial inclusion
- Which events matter most
- What the future looks like under different scenarios

---

## 💡 The Solution

This project delivers a **production-grade financial inclusion analytics and forecasting system** that:

- 📊 Explores historical access and usage trends  
- 🔍 Quantifies the impact of major events (policies, launches, reforms)  
- 🔮 Forecasts financial inclusion outcomes for **2025–2027**  
- 🎯 Enables scenario planning for policy and investment decisions  
- 📈 Presents results through an **interactive Streamlit dashboard**

---

## ✨ Key Features

### 📈 Actionable Policy Insights
Translate complex data into clear forecasts, tables, and visualizations that answer:
- *What will happen?*
- *What should we do next?*

### 🔍 Quantified Event Impact
Measure how **specific events** (e.g., Telebirr launch, M-Pesa entry, FX reforms) affect:
- Account ownership
- Digital payment usage

Delivered via **event–indicator association matrices** with signed impact magnitudes.

### 🔮 Evidence-Based Forecasting
- Forecasts for **2025–2027**
- **Base, optimistic, pessimistic scenarios**
- Confidence intervals and uncertainty discussion
- Sparse-data aware (only 5 Findex points)

### 🎯 Interactive Exploration
A **self-service Streamlit dashboard** allowing non-technical stakeholders to:
- Explore trends
- Compare scenarios
- Download data
- Track progress toward the **60% inclusion target**

### 📊 End-to-End Analysis Pipeline
From raw data → enrichment → EDA → impact modeling → forecasting → dashboard  
All steps are **reproducible via notebooks and scripts**.

---

## 📊 Interactive Dashboard

The dashboard is the **main project output**.

### Dashboard Pages
- 📊 **Overview** – Key metrics, growth highlights
- 📈 **Trends** – Interactive time-series exploration
- 🔮 **Forecasts** – 2025–2027 projections with confidence intervals
- 🎯 **Inclusion Projections** – Progress toward 60% target with scenarios

> 📌 *Add a screenshot or GIF of the dashboard Overview page here if desired.*

### 🚀 Launch Dashboard
```bash
streamlit run dashboard/app.py
```
## 🧠 Key Questions Answered
 - What factors drive financial inclusion in Ethiopia?
 - How do events (policy changes, product launches) affect outcomes?
 - What will financial inclusion look like in 2025–2027?
 - How can policy interventions be optimized?

 # 📁 Project Structure
```bash
ethiopia-financial-inclusion-forecast/
│
├── dashboard/
│   ├── app.py                 # Streamlit dashboard
│   └── readme.md
│
├── data/
│   ├── raw/                   # Raw input data
│   └── processed/
│       ├── enriched_dataset.xlsx
│       └── enrichment_visualization.png
│
├── notebooks/
│   ├── task1_enrichment.ipynb
│   ├── task2_eda_analysis.ipynb
│   ├── task_3_event_impact_modeling.ipynb
│   └── task4_forcasting.ipynb
│
├── reports/
│   ├── figures/
│   ├── event_indicator_matrix.csv
│   ├── task4_access_forecast.csv
│   └── task4_usage_forecast.csv
│
├── src/
│   ├── data/
│   ├── utils/
│   └── __init__.py
│
├── tests/
├── .github/workflows/unittests.yml
├── requirements.txt
├── README.md
├── task2_report.md
├── task3_impact_model_report.md
└── task4_report.md
```

# ⚙️ Installation & Setup
```bash
# Clone repository
git clone https://github.com/bethywa/ethiopia-financial-inclusion-forecast.git

# Create virtual environment
python -m venv venv
venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt
```

# 🧪 Run Full Analysis Pipeline

1. Run notebooks in order:
  - task1_enrichment.ipynb
  - task2_eda_analysis.ipynb
  - task_3_event_impact_modeling.ipynb
  - task4_forcasting.ipynb

2. Review generated reports in /reports

3. Launch dashboard:
   streamlit run dashboard/app.py

   # 📌 Project Status

Status: ✅ Feature Complete
Version: 1.0.0
Last Updated: January 2026

👩‍💻 Developed By

* Bethelihem Weldegebrial
10 Academy / Kifiya AI Master Program

We thank the program instructors and mentors for their guidance and support.


# 🚀 Future Enhancements

 - Gender-disaggregated forecasting
 - Regional (sub-national) inclusion modeling
 - Agent density & infrastructure variables
 - Live data updates via APIs
 - Model comparison dashboard
