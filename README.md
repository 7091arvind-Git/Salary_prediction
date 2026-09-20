💰 Salary Prediction ML Project

Predict the annual salary of employees based on their job-related features using Machine Learning regression models. This project demonstrates an end-to-end workflow including data preprocessing, model training, evaluation, and deployment with Streamlit.

🌐 Live Demo

Try the deployed Streamlit application:

👉 https://7091arvind-git-salary-prediction-app-o0ho30.streamlit.app/

🧩 Project Overview

Goal: Predict annual salaries of employees using historical data.

Dataset Features:

Gender

Years of experience

Department

Country

Center

Job Rate

Sick Leaves

Unpaid Leaves

Overtime Hours

Target: Annual Salary

Models Used

Linear Regression

Decision Tree Regressor

Random Forest Regressor

Gradient Boosting Regressor

Evaluation Metrics

MAE (Mean Absolute Error)

RMSE (Root Mean Squared Error)

R² Score (Coefficient of Determination)

Deployment

The trained model is deployed as an interactive Streamlit application for salary prediction.

📊 Model Comparison

Model

MAE

RMSE

R² Score

Linear Regression

...

...

...

Decision Tree

...

...

...

Random Forest

...

...

...

Gradient Boosting

...

...

...

The best-performing model is saved as best_salary_model.pkl and used by the Streamlit application for predictions.

⚡ How to Run

1. Jupyter Notebook

Open Salary_Prediction_Final.ipynb.

Run all cells to train the models, evaluate their performance, and predict salaries.

The best model will be saved as best_salary_model.pkl.

2. Streamlit App

Install the required dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

Enter the employee details and click Predict Salary.

📂 Project Structure

Salary-Prediction-ML/
│
├── Salary_Prediction_Final.ipynb
├── app.py
├── your_dataset.csv
├── best_salary_model.pkl
├── requirements.txt
└── README.md

📌 Key Features

Compares multiple regression models to identify the best-performing model.

Uses label encoding for categorical variables.

Performs feature analysis using a correlation heatmap.

Saves the best-performing model for deployment.

Provides interactive salary predictions through Streamlit.

🛠️ Tech Stack

Python

Pandas

Scikit-learn

Joblib

Jupyter Notebook

Streamlit

Matplotlib

Seaborn

👨‍💻 Author

Arvind Yadav

GitHub: 7091arvind-Git
Email: 7091arvind@gmail.com

📜 License

This project is open-source and intended for educational purposes.
