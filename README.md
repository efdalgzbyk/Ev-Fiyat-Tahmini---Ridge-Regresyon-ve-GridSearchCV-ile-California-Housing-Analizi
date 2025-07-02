
---

## 🇬🇧 English README

```markdown
# House Price Prediction – Ridge Regression with California Housing Dataset

This project aims to predict housing prices in the state of California using machine learning techniques. A Ridge Regression model is trained on real-world housing data, focusing on regression basics, hyperparameter tuning, and performance visualization.

---

## 📌 Dataset Used

The project uses the California Housing dataset, fetched using `fetch_california_housing()` from `sklearn.datasets`. It includes features such as:

- Average number of rooms
- Average household income
- Crime rate
- Proximity to schools
- Population density
- and more...

Target variable: **House price (in thousands of dollars)**

---

## 🔧 Technologies and Libraries

- Python 3.x
- scikit-learn
- pandas
- matplotlib
- seaborn
- joblib

---

## 🚀 Project Workflow

1. **Data Loading and Exploration:**  
   Load the dataset into a pandas DataFrame and generate a heatmap to analyze feature correlations.

2. **Train-Test Split:**  
   Split the dataset into 80% training and 20% testing sets.

3. **Model Training (Ridge Regression):**  
   Train a Ridge Regression model with hyperparameter optimization (`alpha`) using GridSearchCV.

4. **Model Evaluation:**  
   Evaluate model performance using R² score and Mean Squared Error (MSE).

5. **Prediction Visualization:**  
   Plot predicted vs actual house prices in a scatter plot (`price_prediction_plot.png`).

6. **Model Saving:**  
   Save the trained model to a `.pkl` file (`house_price_model.pkl`).

---

## 📁 Generated Files

- `house_price_prediction.py`: Main project script
- `feature_correlation.png`: Feature correlation heatmap
- `price_prediction_plot.png`: Actual vs predicted price plot
- `house_price_model.pkl`: Saved trained model

---

## 💻 Run the Project

To execute the script, run:

```bash
python house_price_prediction.py
