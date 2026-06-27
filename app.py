import streamlit as st
import pandas as pd
import joblib

# ---------------------------
# Load trained pipeline
# ---------------------------
model = joblib.load("credit_risk_model.pkl")

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Credit Risk Prediction",
    page_icon="💳",
    layout="centered"
)

st.title("💳 Credit Risk Prediction System")
st.write(
    "Enter the applicant's information below to predict whether the loan applicant is **Good Risk** or **Bad Risk**."
)

st.divider()

# ---------------------------
# User Inputs
# ---------------------------

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

sex = st.selectbox(
    "Sex",
    ["male", "female"]
)

job = st.selectbox(
    "Job Level",
    [0, 1, 2, 3],
    help="0 = Unskilled, 3 = Highly Skilled"
)

housing = st.selectbox(
    "Housing",
    ["own", "rent", "free"]
)

saving_accounts = st.selectbox(
    "Saving Account",
    [
        "Unknown",
        "little",
        "moderate",
        "quite rich",
        "rich"
    ]
)

checking_account = st.selectbox(
    "Checking Account",
    [
        "Unknown",
        "little",
        "moderate",
        "rich"
    ]
)

credit_amount = st.number_input(
    "Credit Amount",
    min_value=0,
    value=3000
)

duration = st.number_input(
    "Duration (Months)",
    min_value=1,
    value=24
)

purpose = st.selectbox(
    "Purpose",
    [
        "car",
        "radio/TV",
        "furniture/equipment",
        "business",
        "education",
        "repairs",
        "domestic appliances",
        "vacation/others"
    ]
)

st.divider()

# ---------------------------
# Prediction
# ---------------------------

if st.button("Predict Credit Risk"):

    input_data = pd.DataFrame({

        "Age": [age],
        "Sex": [sex],
        "Job": [job],
        "Housing": [housing],
        "Saving accounts": [saving_accounts],
        "Checking account": [checking_account],
        "Credit amount": [credit_amount],
        "Duration": [duration],
        "Purpose": [purpose]

    })

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == "good":
        st.success("✅ Low Credit Risk (Good Applicant)")
    else:
        st.error("❌ High Credit Risk (Bad Applicant)")