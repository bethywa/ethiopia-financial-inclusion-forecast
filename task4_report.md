# Task 4 Report: Forecasting Financial Access and Digital Payment Usage (2025–2027)

## Project Context
This task forecasts the future trajectory of financial inclusion in Ethiopia, focusing on **account ownership (access)** and **digital payment usage** for the period **2025–2027**.  
The analysis builds on insights from Task 2 (EDA) and Task 3 (event impact modeling), while explicitly acknowledging data sparsity and structural changes in recent years.

---

## 1. Objectives

The objectives of Task 4 are to:

- Forecast **Account Ownership Rate (Access)** for 2025–2027  
- Forecast **Digital Payment Usage** using available proxy data  
- Incorporate uncertainty through **scenario analysis**  
- Interpret results in a policy- and decision-relevant manner  
- Clearly document limitations and assumptions  

---

## 2. Data Constraints and Modeling Implications

### Key Data Limitations
- Only **5 Global Findex survey points** over ~13 years for access
- Usage data is **recent, sparse, and proxy-based**
- Limited gender- and region-disaggregated information
- Structural break observed around **2021–2022**

### Implication
Given these constraints, **simple, transparent models** are more appropriate than complex machine-learning approaches. The focus is on **direction, magnitude, and uncertainty**, not precision.

---

## 3. Forecasting Methodology

### 3.1 Account Ownership (Access)

**Approach**
- Linear trend regression on historical account ownership (2014–2024)
- Adjustment for post-2021 growth slowdown
- Scenario-based extrapolation

**Scenarios**
- **Pessimistic**: Continued stagnation, policy and economic headwinds
- **Base**: Moderate recovery, continuation of recent trends
- **Optimistic**: Successful policy implementation and infrastructure expansion

**Forecast Results**

| Year | Pessimistic (%) | Base (%) | Optimistic (%) |
|-----|----------------|----------|---------------|
| 2025 | 52.7 | 54.7 | 57.7 |
| 2026 | 55.3 | 57.3 | 60.3 |
| 2027 | 57.9 | 59.9 | 62.9 |

---

### 3.2 Digital Payment Usage

**Approach**
- Proxy-based trend extrapolation using recent usage counts
- No reliable long historical baseline available
- Forecast reflects **momentum**, not penetration rates

**Important Note on Scenarios**
Due to limited variation and lack of strong explanatory drivers, **pessimistic, base, and optimistic scenarios converge**.  
This reflects **data limitations**, not a modeling error.

**Forecast Results (Usage Proxy)**

| Year | Pessimistic | Base | Optimistic |
|-----|------------|------|-----------|
| 2025 | 91.6M | 91.6M | 91.6M |
| 2026 | 152.9M | 152.9M | 152.9M |
| 2027 | 214.2M | 214.2M | 214.2M |

These values should be interpreted as **relative growth signals**, not exact population shares.

---

## 4. Interpretation of Results

### 4.1 Account Ownership (Access)

- Ethiopia is projected to **cross 50% account ownership in 2025**
- Base case reaches **~60% by 2027**
- Growth is significantly slower than 2014–2021, confirming **market maturation**
- Remaining unbanked population is harder to reach (rural, low-income, informal)

**Key Insight**  
Future gains will depend less on account creation and more on **activation, trust, and relevance of services**.

---

### 4.2 Digital Payment Usage

- Usage continues to grow rapidly in absolute terms
- Volatility and structural shifts (regulation, competition) dominate patterns
- Scenario differentiation is not statistically defensible with current data

**Key Insight**  
Digital payment systems are expanding, but **usage quality and sustainability** remain uncertain.

---

## 5. Uncertainty and Confidence

### Sources of Uncertainty
- Policy effectiveness (digital ID, interoperability)
- Economic conditions (inflation, currency pressure)
- Regulatory changes
- Infrastructure expansion pace
- Data measurement lag

### How Uncertainty Is Addressed
- Explicit scenario ranges for access
- Cautious interpretation of usage forecasts
- Emphasis on directional rather than point estimates

---

## 6. Strategic Implications

### For Policymakers
- Shift focus from **access → active usage**
- Target last-mile inclusion (rural, women, informal sector)
- Prioritize infrastructure and digital literacy
- Reduce friction in onboarding and compliance

### For Financial Institutions
- Large untapped market remains (~40%)
- Opportunity in product innovation, not just new accounts
- Competition will increasingly be on **service quality**

---

## 7. Key Assumptions

- Linear trends are a reasonable approximation over short horizons
- No major political or economic shocks beyond recent patterns
- Event impacts from Task 3 are directional, not deterministic
- Usage proxy reflects system growth, not individual adoption

---

## 8. Limitations

- Sparse and delayed survey data
- Lack of disaggregated indicators (gender, region)
- Usage modeled via proxy rather than direct survey measure
- Long-term forecasts inherently uncertain

---

## 9. Conclusion

This forecasting exercise presents a **realistic, scenario-aware outlook** for Ethiopia’s financial inclusion trajectory:

- **Access**: Continued progress, but slower and harder
- **Usage**: Rapid expansion with high uncertainty
- **Policy focus**: Quality, activation, and inclusion depth

Rather than precise predictions, the results offer a **decision-support framework** that highlights risks, opportunities, and critical levers for the next phase of financial inclusion in Ethiopia.

---

*End of Task 4 Report*
