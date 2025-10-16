# 💰 Salary Prediction ML Project

Predict the **annual salary of employees** based on their job features using **Machine Learning regression models**. This project demonstrates an end-to-end workflow: data preprocessing, model training, evaluation, and deployment with Streamlit.

---

## 🧩 Project Overview

- **Goal:** Predict annual salaries of employees using historical data.  
- **Dataset Features:**
  - Gender
  - Years of experience
  - Department
  - Country
  - Center
  - Job Rate
  - Sick Leaves
  - Unpaid Leaves
  - Overtime Hours
- **Target:** `Annual Salary`  

- **Models Used:**
  1. Linear Regression
  2. Decision Tree Regressor
  3. Random Forest Regressor
  4. Gradient Boosting Regressor

- **Evaluation Metrics:**
  - MAE (Mean Absolute Error)
  - RMSE (Root Mean Squared Error)
  - R² Score (Coefficient of Determination)

- **Deployment:** Streamlit app for interactive predictions.

---

## 📊 Model Comparison

| Model                  | MAE      | RMSE     | R² Score |
|------------------------|----------|----------|----------|
| Linear Regression      | ...      | ...      | ...      |
| Decision Tree          | ...      | ...      | ...      |
| Random Forest          | ...      | ...      | ...      |
| Gradient Boosting      | ...      | ...      | ...      |

> The best-performing model is **saved** as `best_salary_model.pkl` for deployment in Streamlit.

---

## ⚡ How to Run

### 1. Jupyter Notebook
1. Open `Salary_Prediction_Final.ipynb`.  
2. Run all cells to train models, evaluate, and predict new salaries.  
3. The best model will be saved automatically as `best_salary_model.pkl`.

### 2. Streamlit App
1. Install Streamlit if not already installed:
```bash
pip install streamlit
### 2.Run the app:

streamlit run app.py
### 3.Enter employee details and click Predict Salary.

🔧 Project Structure
Salary-Prediction-ML/
│
├─ Salary_Prediction_Final.ipynb  # Jupyter Notebook with training & evaluation
├─ app.py                        # Streamlit app
├─ your_dataset.csv              # Dataset used for training
├─ best_salary_model.pkl         # Saved best ML model
└─ README.md                     # Project description
📌 Key Features

Compares multiple ML models to select the best one automatically.

Uses label encoding for categorical variables.

Generates correlation heatmap for feature analysis.

Deployable as interactive web app using Streamlit.
⚡ Author

Arvind Yadav

GitHub: 7091arvind-Git

Email: 7091arvind@gmail.com
📜 License

This project is open-source. Feel free to use and modify for educational purposes.




