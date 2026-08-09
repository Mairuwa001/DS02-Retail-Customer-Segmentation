import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/customer_segmentation_model.pkl")
scaler = joblib.load("models/rfm_scaler.pkl")

segment_map = {
    0: "Regular Customers",
    1: "At-Risk / Inactive Customers",
    2: "VIP Loyal Customers",
    3: "High-Value Loyal Customers",
    4: "Elite VIP Customers"
}

recommendations = {
    "Regular Customers": "Use loyalty offers, cross-selling and personalized promotions to increase purchase frequency and value.",
    "At-Risk / Inactive Customers": "Use re-engagement campaigns, targeted discounts and reminders to encourage repeat purchases.",
    "VIP Loyal Customers": "Prioritize retention with exclusive benefits, personalized offers and early access to new products.",
    "High-Value Loyal Customers": "Strengthen retention through loyalty rewards, personalized communication and premium offers.",
    "Elite VIP Customers": "Provide highly personalized service, exclusive experiences and priority support to protect their high revenue contribution."
}

st.set_page_config(
    page_title="Retail Customer Segmentation",
    page_icon="📊",
    layout="centered"
)

st.title("Retail Customer Segmentation")
st.write("Use customer RFM information to identify the most relevant customer segment.")

st.subheader("Customer Information")

recency = st.number_input("Recency (days since last purchase)", min_value=1.0, value=30.0, step=1.0)
frequency = st.number_input("Frequency (number of purchases)", min_value=1.0, value=5.0, step=1.0)
monetary = st.number_input("Monetary Value (total customer spend)", min_value=0.0, value=1000.0, step=50.0)

if st.button("Predict Customer Segment", type="primary"):
    customer = pd.DataFrame({
        "Recency": [recency],
        "Frequency": [frequency],
        "Monetary": [monetary]
    })

    scaled_customer = scaler.transform(customer)
    cluster = int(model.predict(scaled_customer)[0])
    segment = segment_map.get(cluster, f"Cluster {cluster}")

    st.success(f"Customer Segment: {segment}")

    col1, col2, col3 = st.columns(3)
    col1.metric("Recency", f"{recency:.0f} days")
    col2.metric("Frequency", f"{frequency:.0f}")
    col3.metric("Monetary", f"{monetary:,.2f}")

    st.subheader("Recommended Action")
    st.write(recommendations[segment])

st.divider()
st.caption("DS-02 Retail Customer Segmentation | K-Means clustering using RFM features")
