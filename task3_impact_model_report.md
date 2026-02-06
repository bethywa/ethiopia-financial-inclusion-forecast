# Task 3 Report: Event–Indicator Impact Modeling

## Project Context
This task develops a structured framework to translate major policy, market, and product events in Ethiopia’s financial ecosystem into their expected impacts on key financial inclusion indicators. The goal is not to forecast exact numerical outcomes, but to encode expert judgment and empirical evidence into a transparent, explainable impact model that can later support scenario analysis and forecasting.

---

## 1. Methodology

### 1.1 Conceptual Approach
Task 3 implements an **event-to-indicator impact mapping** approach. Each major event (e.g., product launches, regulatory reforms, market entries) is assumed to influence one or more financial inclusion indicators.

For each event–indicator pair, three attributes are defined:

- **Impact direction**: increase or decrease
- **Impact magnitude**: low, medium, or high
- **Impact weight**: numerical encoding of magnitude and direction

This information is represented as an **impact matrix**, where:
- Rows represent events
- Columns represent indicators
- Cell values represent signed impact weights

This structure enables transparent reasoning about how different interventions interact with financial inclusion outcomes.

---

### 1.2 Functional Form

Impacts are encoded using a **linear additive functional form**:

\[
Impact_{event, indicator} = Sign \times Weight
\]

Where:
- `Sign = +1` for positive impacts, `-1` for negative impacts
- `Weight = {0.5, 1.0, 2.0}` corresponding to {low, medium, high} impact magnitude

This produces a sparse impact matrix suitable for:
- Visualization (heatmaps)
- Aggregation across events
- Downstream scenario modeling (Task 4)

This functional form was chosen because it is:
- Interpretable to non-technical stakeholders
- Easy to validate and extend
- Consistent with expert-judgment-based policy models

---

## 2. Data Sources

### 2.1 Event and Impact Link Data
Impact relationships were sourced from the curated enriched dataset:

- **Events sheet**: Defines policy, product, and market events (e.g., Telebirr launch, FX reform)
- **Impact links sheet**: Defines relationships between events and indicators, including:
  - Impact direction
  - Impact magnitude
  - Evidence basis
  - Lag assumptions
  - Comparable country references

---

### 2.2 Evidence Sources for Impact Estimates

Impact estimates are grounded in three primary evidence types:

1. **Empirical evidence**
   - Observed trends in Ethiopia or comparable markets
   - Usage growth following mobile money launches
   - Telecom competition effects on coverage and pricing

2. **Literature-based evidence**
   - World Bank and GSMA financial inclusion studies
   - Cross-country comparisons (e.g., Kenya, Rwanda)
   - Academic research on digital finance adoption

3. **Expert judgment**
   - Domain-informed assumptions where empirical data is limited
   - Policy analysis of regulatory and macroeconomic reforms

Each impact link records its evidence basis to maintain traceability.

---

## 3. Validation Against Observed Data

### 3.1 Validation Strategy
Validation was conducted by comparing:
- **Predicted impact directions** from the impact matrix
- **Observed indicator trends** in historical time-series data

The validation focuses on:
- Directional consistency (increase vs decrease)
- Relative strength across indicators
- Temporal plausibility given assumed lags

---

### 3.2 Validation Results

Key observations:

- Indicators associated with **digital financial products** (e.g., Telebirr, M-Pesa) generally show upward long-term trends, consistent with positive impact assumptions.
- Indicators related to **affordability and macroeconomic conditions** (e.g., data affordability) show volatility and occasional declines, aligning with negative impacts from FX reforms and price shocks.
- Short-term deviations between predicted and observed values are expected due to:
  - Lag effects
  - External shocks (e.g., inflation, COVID-19)
  - Concurrent events affecting the same indicator

Overall, observed data trends are **directionally consistent** with the modeled impacts, supporting the validity of the impact matrix as a qualitative decision-support tool.

---

## 4. Key Assumptions

The Task 3 model relies on the following assumptions:

1. **Linearity**
   - Impacts from multiple events combine additively.
   - Interaction effects are not explicitly modeled at this stage.

2. **Relative, Not Absolute Effects**
   - Impact weights reflect relative strength, not exact numerical changes.

3. **Lag Simplification**
   - Lag effects are acknowledged but not dynamically modeled in this task.

4. **Ceteris Paribus Interpretation**
   - Impacts represent isolated event effects, assuming other factors remain constant.

---

## 5. Uncertainties and Limitations

Key sources of uncertainty include:

- **Attribution uncertainty**
  - Multiple events often affect the same indicator simultaneously.
- **Data quality limitations**
  - Sparse or irregular historical data for some indicators.
- **Contextual differences**
  - Comparable country evidence may not fully transfer to Ethiopia.
- **Behavioral responses**
  - User adoption and market responses may differ from expectations.

These uncertainties are explicitly documented to ensure transparency and guide cautious interpretation.

---

## 6. Conclusion

Task 3 successfully translates qualitative and empirical knowledge about Ethiopia’s financial ecosystem into a structured, explainable impact model. The resulting impact matrix provides a critical foundation for:

- Scenario analysis
- Policy evaluation
- Quantitative forecasting in Task 4

Rather than claiming precise causality, the model offers a disciplined way to reason about how major events shape financial inclusion outcomes over time.
