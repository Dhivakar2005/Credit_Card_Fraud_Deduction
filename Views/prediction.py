import streamlit as st
import pandas as pd
import joblib

def prediction():
# -------------------- Load Model and Scaler --------------------
    model = joblib.load("models/fraud_model.joblib")
    scaler = joblib.load("models/scaler.pkl")

    # Define full list of model features
    model_features = ['V' + str(i) for i in range(1, 29)] + ['Amount']

    # -------------------- Page 2: Prediction --------------------
    st.title("💸 Single Transaction")
    st.write("Enter transaction details below to predict if it's **fraudulent or legitimate**:")

    # User inputs for selected features
    user_inputs = {
            'V1': st.number_input("V1", value=0.0),
            'V2': st.number_input("V2", value=0.0),
            'V3': st.number_input("V3", value=0.0),
            'V4': st.number_input("V4", value=0.0),
            'V14': st.number_input("V14", value=0.0),
            'Amount': st.number_input("Amount", value=0.0)
        }

    # Prepare full input
    input_data = {feature: 0 for feature in model_features}
    for key, value in user_inputs.items():
        if key == 'Amount':
            try:
                value = scaler.transform([[value]])[0][0]
            except:
                st.warning("⚠️ Could not scale Amount — using raw value.")
        input_data[key] = value

    df_input = pd.DataFrame([input_data])

    if st.button("🚨 Predict Fraud"):
        try:
            prediction = model.predict(df_input)[0]
            confidence = model.predict_proba(df_input)[0][1]
            if prediction == 1:
                st.error(f"⚠️ Fraudulent Transaction Detected! (Confidence: {confidence:.2f})")
            else:
                st.success(f"✅ Legitimate Transaction (Confidence: {1 - confidence:.2f})")
        except Exception as e:
            st.error(f"🚫 Prediction Failed: {e}")