import streamlit as st

# -------------------- Page 1: Home --------------------
def home():
    st.title("DetectWise 💳")
    st.write("""
        Welcome to **DetectWise**, your intelligent assistant for detecting fraudulent credit card transactions using machine learning.

        This app leverages a trained model to analyze transaction data and identify patterns commonly associated with fraud.

        ### 🔎 What Can You Do?
        - **Single Prediction:** Enter a few transaction details to instantly check whether it's fraudulent.
        - **Bulk Prediction:** Upload a CSV file of multiple transactions to evaluate them all at once.

        ### 🧠 How It Works
        - We use **Principal Component Analysis (PCA)** to reduce dimensionality and protect sensitive data.
        - The model evaluates anonymized features: **V1 to V28**.
        - The **Amount** of the transaction is also considered in the prediction.

        ### ⚠️ Please Note:
        - The V1–V28 features are **PCA-transformed** and anonymized to protect user privacy.
        - The model was trained on the [Kaggle Credit Card Fraud Detection dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud).
        - This tool is for **educational and demonstration** purposes only.

        👉 Use the **sidebar** to navigate between the available tools.
        """)