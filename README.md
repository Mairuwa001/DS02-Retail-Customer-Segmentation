# DS-02 Retail Customer Segmentation

## Project Overview
This project develops a machine-learning MVP that segments retail customers using **RFM analysis** and **K-Means clustering**. It is designed to help retail/POS businesses move from treating all customers alike to using data-driven customer engagement strategies.

## Problem Statement
Retailers often overgeneralize customers and use the same marketing approach for everyone. This can lead to missed opportunities to retain valuable customers, reactivate inactive customers, and improve loyalty.

## Objectives
- Clean and prepare transaction data.
- Calculate Recency, Frequency and Monetary (RFM) features.
- Standardize the RFM features.
- Apply K-Means clustering.
- Evaluate and profile the clusters.
- Provide business recommendations.
- Deliver a working Streamlit MVP.

## Dataset
The project uses transaction-level retail data containing customer, transaction date, quantity, price and product information.

After cleaning:
- **392,692** valid transaction rows remained.
- **4,338** customers were available for customer-level segmentation.
- The final customer-level analysis contains **18,532** transactions.

## Methodology

### Data Preparation
Missing values, invalid quantities, invalid prices and other data-quality issues were handled before customer-level analysis.

### RFM Analysis
- **Recency:** days since the customer's most recent purchase.
- **Frequency:** number of purchases/transactions.
- **Monetary:** total customer spending.

### Standardization
RFM features were standardized before clustering. The fitted scaler is saved as `models/rfm_scaler.pkl`.

### K-Means Clustering
Different cluster sizes were evaluated and **5 customer segments** were selected for the final MVP. The trained model is saved as `models/customer_segmentation_model.pkl`.

### Evaluation
The final solution achieved a **Silhouette Score of approximately 0.6165**, indicating reasonably separated customer groups.

## Customer Segments

| Segment | Customers | Revenue Share |
|---|---:|---:|
| Regular Customers | 3,048 | 45.72% |
| At-Risk / Inactive Customers | 1,063 | 5.73% |
| High-Value Loyal Customers | 213 | 30.71% |
| VIP Loyal Customers | 8 | 4.96% |
| Elite VIP Customers | 6 | 12.88% |

A key finding is that a relatively small group of high-value customers contributes a substantial share of revenue, supporting differentiated retention strategies.

## Business Recommendations

**Regular Customers:** loyalty offers, cross-selling and personalized promotions.

**At-Risk / Inactive Customers:** re-engagement campaigns, targeted discounts and reminders.

**High-Value Loyal Customers:** retention rewards, personalized communication and premium offers.

**VIP Loyal Customers:** exclusive benefits, personalized offers and early access.

**Elite VIP Customers:** highly personalized service, exclusive experiences and priority support.

## Working MVP

The Streamlit application in `app.py` allows a user to enter:
- Recency
- Frequency
- Monetary value

The trained model predicts the customer segment and provides a recommended business action.

### Run locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

## Project Structure

```text
DS02-Retail-Customer-Segmentation/
├── app.py
├── DS02_Retail_Customer_Segmentation.ipynb
├── README.md
├── requirements.txt
├── models/
│   ├── customer_segmentation_model.pkl
│   └── rfm_scaler.pkl
└── outputs/
    ├── final_customer_segments.csv
    └── segment_profile.csv
```

## Nigerian Context
The MVP addresses a practical retail challenge: limited marketing resources must be directed toward the customers and behaviours that matter most. A Nigerian POS or retail business could use these segments to prioritize re-engagement, loyalty and high-value customer retention.

## Limitations
- Uses historical transaction behaviour.
- Uses RFM features rather than demographics or product preferences.
- Recommendations are rule-based interpretations of the clusters.
- Customer intent and future behaviour are not directly modeled.

## Future Improvements
- Add product-category preferences.
- Add customer lifetime value estimation.
- Add campaign-response prediction.
- Connect to live POS data.
- Add an interactive business dashboard.
- Monitor movement between segments over time.

## Technologies
Python, Pandas, Scikit-learn, Joblib, Streamlit and Jupyter Notebook.

## Deliverables
Analysis notebook, trained model, scaler, segmentation outputs, Streamlit MVP, documentation and 2–3 minute demonstration video.
