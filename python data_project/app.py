from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and support files
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')
interest_map = joblib.load('interest_map.pkl')
feature_names = joblib.load('input_features.pkl')
interest_map_rev = {v: k for k, v in interest_map.items()}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        input_data = {
            'Pregnancies': int(request.form['Pregnancies']),
            'Glucose': int(request.form['Glucose']),
            'BloodPressure': int(request.form['BloodPressure']),
            'SkinThickness': int(request.form['SkinThickness']),
            'Insulin': int(request.form['Insulin']),
            'BMI': float(request.form['BMI']),
            'DiabetesPedigreeFunction': float(request.form['DiabetesPedigreeFunction']),
            'Age': int(request.form['Age']),
        }

        # Create input array
        input_vector = np.array([input_data[feature] for feature in feature_names]).reshape(1, -1)
        input_vector_scaled = scaler.transform(input_vector)

        # Predict
        pred = model.predict(input_vector_scaled)[0]
        prediction = interest_map_rev.get(pred, "Unknown")

    except Exception as e:
        prediction = f"Error: {e}"

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
