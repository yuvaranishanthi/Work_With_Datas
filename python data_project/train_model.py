import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib

# Load the dataset
data = pd.read_csv('pima_diabetes_data.csv')

# Create interest_map to encode Outcome labels (optional, helpful if Outcome is not 0/1)
interest_names = data['Outcome'].unique()
interest_map = {value: idx for idx, value in enumerate(interest_names)}

# Encode the target
data['Interest_encoded'] = data['Outcome'].map(interest_map)

# Select features and target
X = data[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
          'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
y = data['Interest_encoded']

# Apply scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_scaled, y)

# Save model and components
joblib.dump(model, 'model.pkl')                   # trained model
joblib.dump(scaler, 'scaler.pkl')                 # scaler for input normalization
joblib.dump(X.columns.tolist(), 'input_features.pkl')  # feature order
joblib.dump(interest_map, 'interest_map.pkl')     # label mapping

print("✅ Model, scaler, and metadata saved successfully.")
