# Retail Customer Segmentation

## NextGen 3MTT Data Science Capstone — DS 02

### Project Overview

Retail businesses often treat all customers similarly despite differences in purchasing behaviour. This can lead to ineffective marketing, customer retention, and loyalty strategies.

This project develops a customer segmentation MVP for a POS/retail business using transaction data. Customers are grouped according to their purchasing behaviour using RFM analysis and K-Means clustering.

### Problem Context

Many retailers in Nigeria collect transaction data through POS systems but may not fully use this data to distinguish between different types of customers.

This project demonstrates how transaction data can be transformed into actionable customer segments that can support targeted customer engagement and business decisions.

### Objectives

The project aims to:

- Prepare and clean retail transaction data.
- Calculate customer-level Recency, Frequency, and Monetary values.
- Group customers using K-Means clustering.
- Evaluate the quality of the clustering.
- Profile the resulting customer segments.
- Identify revenue contribution by segment.
- Provide practical recommendations for different customer groups.

### Dataset

The project uses the Online Retail Dataset obtained from Kaggle.

The raw dataset contains 541,909 transaction records.

The dataset includes:

- Invoice number
- Product description
- Quantity
- Invoice date
- Unit price
- Customer ID
- Country

The raw dataset is not included in the repository because of its size.

### Methodology

The project follows this workflow:

Data Acquisition → Data Cleaning → Exploratory Data Analysis → RFM Analysis → Feature Standardization → K-Means Clustering → Evaluation → Customer Profiling → Business Recommendations

### Data Preparation

The data was cleaned by:

- Removing records without CustomerID.
- Removing cancelled invoices.
- Removing transactions with non-positive quantities.
- Removing transactions with non-positive unit prices.
- Removing duplicate records.
- Calculating transaction-level revenue.

After cleaning, 392,692 valid transaction records remained, representing 4,338 customers and 18,532 unique invoices.

### RFM Analysis

RFM analysis was used to summarize customer purchasing behaviour.

- Recency: Number of days since the customer's most recent purchase.
- Frequency: Number of unique invoices associated with the customer.
- Monetary: Total amount spent by the customer.

### Clustering

K-Means clustering was applied to the standardized RFM features.

Different cluster sizes were evaluated using the Silhouette Score.

The final model uses 5 customer clusters.

### Model Evaluation

The final five-cluster solution achieved a Silhouette Score of 0.6165, indicating reasonably well-defined customer groupings.

### Customer Segments

| Segment | Customers | Customer Share | Revenue Share |
|---|---:|---:|---:|
| Regular Customers | 3,048 | 70.26% | 45.72% |
| At-Risk / Inactive Customers | 1,063 | 24.50% | 5.73% |
| High-Value Loyal Customers | 213 | 4.91% | 30.71% |
| VIP Loyal Customers | 8 | 0.18% | 4.96% |
| Elite VIP Customers | 6 | 0.14% | 12.88% |

### Key Findings

High-Value Loyal, VIP Loyal, and Elite VIP customers represent approximately 5.23% of customers but contribute approximately 48.55% of total revenue.

At-Risk / Inactive customers represent 24.50% of customers but contribute only 5.73% of revenue.

These findings demonstrate why treating all customers as one group may result in inefficient customer engagement strategies.

### Business Recommendations

**Regular Customers**

Use personalized promotions, cross-selling, and loyalty incentives to encourage repeat purchases and increase customer value.

**At-Risk / Inactive Customers**

Use targeted re-engagement campaigns and time-limited incentives to encourage customers to return.

**High-Value Loyal Customers**

Prioritize retention, personalized offers, loyalty rewards, and premium product recommendations.

**VIP Loyal Customers**

Provide exclusive benefits, early access to products, and highly personalized engagement.

**Elite VIP Customers**

Provide highly personalized service and retention strategies because this small group contributes a significant share of revenue.

### PCA

Principal Component Analysis was used to visualize the customer clusters in two dimensions.

PC1 explains 55.47% of the variance and PC2 explains 30.25%. Together, the two components explain 85.73% of the variance in the standardized RFM features.

### Limitations

The analysis is based on historical transaction data and therefore reflects past customer behaviour.

The dataset is not Nigerian retail data. The Nigerian context is used to demonstrate how the methodology could be applied to POS and retail businesses in Nigeria.

### Future Improvements

Future versions could incorporate:

- Nigerian POS transaction data.
- Customer lifetime value prediction.
- Product recommendation systems.
- Automated dashboards.
- Integration with POS systems.
- Periodic model retraining.

### Tools

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- Jupyter / Google Colab

### Deliverables

- Data science notebook
- Trained K-Means model
- RFM feature scaler
- Customer segmentation output
- Segment profile
- Project documentation
- 2–3 minute demonstration video

### Author

Khalil Bilyaminu

NextGen 3MTT Data Science Fellow
