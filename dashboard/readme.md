# Task 5: Financial Inclusion Dashboard

This task implements an interactive **Streamlit dashboard** to visualize financial inclusion forecasts for Ethiopia.

## Objective
Enable stakeholders to:
- View account ownership forecasts (2025–2027)
- Compare optimistic, base, and pessimistic scenarios
- Track progress toward the 60% financial inclusion target
- Download forecast data

## Data Used
- `reports/task4_access_forecast.csv`  
  (Forecast outputs from Task 4)

## Features
- Interactive scenario selection
- Forecast line chart with target indicator
- Scenario comparison table
- Progress bar toward inclusion target
- Data download option


## How to Run
```bash
pip install streamlit pandas plotly
cd dashboard
streamlit run app.py
