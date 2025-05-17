import streamlit as st
from streamlit_option_menu import option_menu
from Views.home import home
from Views.prediction import prediction
from Views.bulkprediction import bulk_prediction

# --- Optional: Display logo ---
st.logo("logo.png")

# --- Sidebar Navigation ---
with st.sidebar:
    pg = option_menu(
        menu_title="Menu",
        options=["Home", "Prediction", "Bulk Prediction"],
        icons=["house", "graph-up", "cloud-upload"],
        menu_icon="cast",
        default_index=0,
    )

# --- Run Page Based on Selection ---
if pg == "Home":
    home()
elif pg == "Prediction":
    prediction()
elif pg == "Bulk Prediction":
    bulk_prediction()
