import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Ethiopia Financial Inclusion Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("🇪🇹 Ethiopia Financial Inclusion Forecast Dashboard")
st.markdown("Forecasting financial inclusion (Account Ownership) for 2025–2027")
st.markdown("---")

# --------------------------------------------------
# Load data
# --------------------------------------------------
@st.cache_data
def load_forecast_data():
    path = "../reports/task4_access_forecast.csv"
    return pd.read_csv(path)

df = load_forecast_data()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.header("⚙️ Controls")

scenario = st.sidebar.selectbox(
    "Select Scenario",
    ["base", "optimistic", "pessimistic"]
)

target_rate = st.sidebar.slider(
    "Target Financial Inclusion (%)",
    min_value=50,
    max_value=70,
    value=60
)

# --------------------------------------------------
# Overview section
# --------------------------------------------------
st.header("📊 Overview")

latest_year = df["year"].max()
latest_value = df[df["year"] == latest_year][scenario].values[0]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Latest Year", latest_year)

with col2:
    st.metric(
        f"{scenario.capitalize()} Projection ({latest_year})",
        f"{latest_value:.1f}%"
    )

with col3:
    gap = target_rate - latest_value
    if gap <= 0:
        st.metric("Target Status", "Achieved ✅")
    else:
        st.metric("Gap to Target", f"{gap:.1f} pp")

# --------------------------------------------------
# Forecast visualization
# --------------------------------------------------
st.header("🔮 Forecast Scenarios")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df["year"],
    y=df["base"],
    mode="lines+markers",
    name="Base",
    line=dict(width=3)
))

fig.add_trace(go.Scatter(
    x=df["year"],
    y=df["optimistic"],
    mode="lines+markers",
    name="Optimistic",
    line=dict(dash="dot")
))

fig.add_trace(go.Scatter(
    x=df["year"],
    y=df["pessimistic"],
    mode="lines+markers",
    name="Pessimistic",
    line=dict(dash="dot")
))

fig.add_hline(
    y=target_rate,
    line_dash="dash",
    annotation_text=f"{target_rate}% Target",
    annotation_position="right"
)

fig.update_layout(
    title="Account Ownership Forecast (2025–2027)",
    xaxis_title="Year",
    yaxis_title="Account Ownership (%)",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# Scenario comparison table
# --------------------------------------------------
st.header("📋 Scenario Comparison Table")

comparison = df.copy()
comparison["Range"] = comparison["optimistic"] - comparison["pessimistic"]

st.dataframe(
    comparison.style.format("{:.1f}"),
    use_container_width=True
)

# --------------------------------------------------
# Progress toward target
# --------------------------------------------------
st.header("🎯 Progress Toward Target")

progress = min(latest_value / target_rate, 1.0)

st.progress(progress)

if progress >= 1:
    st.success("🎉 Financial inclusion target achieved!")
else:
    st.info(f"📈 {progress*100:.1f}% of target achieved")

# --------------------------------------------------
# Download data
# --------------------------------------------------
st.header("⬇️ Download Data")

csv = df.to_csv(index=False)
st.download_button(
    label="Download Forecast Data (CSV)",
    data=csv,
    file_name="task4_access_forecast.csv",
    mime="text/csv"
)
