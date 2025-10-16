# ======================================
# Salary Prediction Streamlit App
# Models: Linear, Decision Tree, Random Forest, Gradient Boosting
# ======================================

import streamlit as st
import pandas as pd
import joblib

# ======================================
# Load Model
# ======================================
model = joblib.load("best_salary_model.pkl")

# ======================================
# Streamlit UI
# ======================================
st.set_page_config(page_title="Salary Prediction App", layout="centered")
st.title("💰 Employee Salary Prediction App")
st.write("Predict employee's **annual salary** using trained ML models.")

st.divider()
st.header("Enter Employee Details")

gender = st.selectbox("Gender", ["Male", "Female"])
years = st.number_input("Years of Experience", min_value=0, max_value=40, value=2)
department = st.selectbox("Department", [
    "Quality Control", "Manufacturing", "Major Mfg Projects", "Research", "HR", "Finance"
])
country = st.selectbox("Country", [
    "Saudi Arabia", "Egypt", "United Arab Emirates", "India", "Other"
])
center = st.selectbox("Center", ["Main", "West", "East"])
job_rate = st.slider("Job Rate", 1.0, 5.0, 3.0)
sick_leaves = st.number_input("Sick Leaves", min_value=0, max_value=50, value=1)
unpaid_leaves = st.number_input("Unpaid Leaves", min_value=0, max_value=50, value=0)
overtime_hours = st.number_input("Overtime Hours", min_value=0, max_value=300, value=100)

# Encoding (must match training)
gender_map = {"Male": 1, "Female": 0}
dept_map = {
    "Quality Control": 0,
    "Manufacturing": 1,
    "Major Mfg Projects": 2,
    "Research": 3,
    "HR": 4,
    "Finance": 5
}
country_map = {
    "Saudi Arabia": 0,
    "Egypt": 1,
    "United Arab Emirates": 2,
    "India": 3,
    "Other": 4
}
center_map = {"Main": 0, "West": 1, "East": 2}

input_data = pd.DataFrame({
    "Gender": [gender_map[gender]],
    "Years": [years],
    "Department": [dept_map.get(department, 0)],
    "Country": [country_map.get(country, 0)],
    "Center": [center_map.get(center, 0)],
    "Job Rate": [job_rate],
    "Sick Leaves": [sick_leaves],
    "Unpaid Leaves": [unpaid_leaves],
    "Overtime Hours": [overtime_hours]
})

# ======================================
# Prediction
# ======================================
if st.button("🔮 Predict Salary"):
    predicted_salary = model.predict(input_data)[0]
    st.success(f"### 💵 Predicted Annual Salary: ₹{predicted_salary:,.2f}")
    st.info("Model used: Best selected from Linear, Decision Tree, Random Forest, Gradient Boosting")
    st.balloons()
