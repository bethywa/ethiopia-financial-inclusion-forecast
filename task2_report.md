
# Task 2: Exploratory Data Analysis (EDA)
**Financial Inclusion in Ethiopia (2011–2024)**

_Last updated: 2026-02-05 23:49:16_

---

## Objective
The objective of this exploratory analysis is to understand historical patterns, structural changes, and key drivers of financial inclusion in Ethiopia, with a focus on access, usage, infrastructure, and major policy or market events. The analysis also identifies data limitations and generates hypotheses for subsequent impact modeling.

---

## Dataset Overview

### Record Types
- **Observations:** 45  
- **Events:** 13  
- **Targets:** 3  

The dataset is observation-heavy, making it suitable for trend and time-series analysis, while event records enable contextual interpretation.

### Pillar Coverage
- **Access:** Strongest coverage (account ownership, mobile money)
- **Usage:** Limited and recent
- **Gender & Affordability:** Sparse
- **Infrastructure & Enablers:** Moderate, mostly post-2022

This structure implies that access trends can be modeled with confidence, while equity and usage depth analyses are constrained.

---

## Data Quality Assessment
- Majority of records are labeled **high confidence**
- No low-confidence observations
- Sources include IMF FAS, World Bank Findex, GSMA, WHO, and national institutions

Overall data reliability is high, but temporal completeness varies across indicators.

---

## Temporal Coverage Analysis
- Account ownership has consistent coverage from **2011–2024**
- Mobile money indicators emerge post-2018
- Infrastructure and affordability indicators appear mainly after 2022
- Gender-disaggregated data is extremely limited

**Implication:** Long-term modeling is reliable primarily for access indicators.

---

## Access Analysis

### Account Ownership Trend (2011–2024)
- Rapid growth between **2014–2018**
- Structural slowdown after **2021**

### Growth Rates
- Pre-2021 average: ~**+3.1 pp/year**
- Post-2021 average: ~**+1.0 pp/year**

This represents a clear structural break rather than a short-term fluctuation.

---

## Usage and Digital Payments

### Mobile Money Penetration
- Strong growth after 2018
- High volatility between years
- 2021 dip likely reflects changes in measurement or definitions

**Key Insight:** Mobile money account growth does not translate directly into increased financial inclusion.

---

## Infrastructure and Enablers
Available indicators include:
- ATM density
- Branch density
- Connectivity-related proxies

Scatter analysis shows weak correlation between infrastructure averages and account ownership growth, suggesting diminishing marginal returns of infrastructure expansion.

---

## Event Timeline Analysis
Key events include:
- Telebirr launch (May 2021)
- Safaricom market entry (Aug 2022)
- M-Pesa launch (Aug 2023)
- COVID-19 related policy measures

Despite increased event density, account ownership growth remained subdued post-2021, indicating limited immediate impact of these interventions.

---

## Correlation Analysis
- Access and mobile money indicators show directional alignment
- Affordability metrics appear negatively associated with access
- Correlation strength is limited by small overlapping samples

Correlations should be interpreted as indicative rather than causal.

---

## Key Insights

1. Account ownership is most reliable indicator for long-term analysis.
2. Financial inclusion growth slowed sharply after 2021.
3. Mobile money expansion has decoupled from inclusion outcomes.
4. Infrastructure availability alone no longer predicts access gains.
5. Event-driven reforms have shown diminishing returns.
6. Gender and usage depth data gaps limit equity analysis.

---

## Data Gaps and Limitations
- Sparse gender-disaggregated data
- Limited historical usage metrics
- Recent-only infrastructure indicators
- Inconsistent indicator definitions across sources

These constraints limit causal inference and require cautious interpretation.

---

## Implications for Impact Modeling (Task 3)
- Structural breaks must be explicitly modeled
- Infrastructure variables should be treated as leading indicators
- Event-based impact analysis is preferable to linear trends
- Hypothesis-driven modeling is required

---

**Status:** ✅ Task 2 EDA completed and documented
