import streamlit as st
import numpy as np
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

def bulk_prediction():
    # -------------------- Load Model and Scaler --------------------
    model = joblib.load("models/fraud_model.joblib")
    scaler = joblib.load("models/scaler.pkl")

    # Define full list of model features
    model_features = ['V' + str(i) for i in range(1, 29)] + ['Amount']


    # -------------------- Page 3: Bulk Prediction --------------------

    st.title("📊 Bulk Fraud Prediction")
    st.write("Upload a CSV containing PCA-transformed transaction features (V1–V28) Amount , and optionally  Class to detect and analyze fraud at scale.")

    uploaded_file = st.file_uploader("📁 Upload CSV File", type=["csv"])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)

                # Validate required columns
            missing = [col for col in model_features if col not in df.columns]
            if missing:
                st.error(f"❌ Missing columns: {', '.join(missing)}")
            else:
                df_processed = df.copy()

                # Scale Amount
                try:
                    df_processed['Amount'] = scaler.transform(df[['Amount']])
                except:
                    st.warning("⚠️ Could not scale Amount — using raw values.")

                    # Use preloaded model to predict
                predictions = model.predict(df_processed[model_features])
                probabilities = model.predict_proba(df_processed[model_features])[:, 1]

                    # Append predictions
                df['Prediction'] = predictions
                df['Fraud_Confidence'] = probabilities
                df['Label'] = df['Prediction'].apply(lambda x: "Fraud" if x == 1 else "Legit")

                    # Display results
                st.success("✅ Predictions complete!")
                st.dataframe(df.head())

                # Metrics summary
                fraud_count = np.sum(predictions)
                total = len(predictions)
                legit_count = total - fraud_count
                fraud_percent = (fraud_count / total) * 100

                col1, col2, col3 = st.columns(3)
                col1.metric("Total Transactions", total)
                col2.metric("Predicted Frauds", fraud_count, f"{fraud_percent:.2f}%")
                col3.metric("Predicted Legit", legit_count)

                # EDA Visualizations
                st.subheader("📊 EDA: Fraud vs Legit")
                fraud_counts = df['Label'].value_counts()
                fig1, ax1 = plt.subplots()
                ax1.pie(fraud_counts, labels=fraud_counts.index, autopct='%1.1f%%', startangle=90,
                        colors=['#66BB6A', '#EF5350'])
                ax1.axis('equal')
                st.pyplot(fig1)

                # Download results
                csv_out = df.to_csv(index=False).encode("utf-8")
                st.download_button("📥 Download Results", csv_out, "fraud_predictions.csv", "text/csv")

                # Retrain in background if 'Class' is present
                if 'Class' in df.columns:
                    st.info("🔁 Retraining the model..!")
                    try:
                        X = df_processed[model_features]
                        y = df['Class']
                        X_train, X_test, y_train, y_test = train_test_split(
                            X, y, test_size=0.2, stratify=y, random_state=42
                        )

                        retrained_model = RandomForestClassifier(
                            n_estimators=100, random_state=42, class_weight='balanced'
                        )
                        retrained_model.fit(X_train, y_train)

                        # Optionally: Save the model or update global model (if needed)
                        # model = retrained_model  # uncomment to replace global model
                        st.success("✅ Model retraining complete.")

                    except Exception as e:
                        st.error(f"❌ Background retraining failed: {e}")

        except Exception as e:
            st.error(f"🚫 Error processing file: {e}")
