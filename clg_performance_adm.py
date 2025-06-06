# -*- coding: utf-8 -*-
"""clg_performance_adm.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xJKOh1F5UDwcHvm6GksniXV6AWTNwF1I
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

!pip install scikit-learn

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

from google.colab import files
uploaded=files.upload()

df=pd.read_csv('Clg_peform.csv')
print(df.head())

import seaborn as sns
sns.boxplot(df['Entrance Test Score'])

df['Entrance Test Score'] = pd.to_numeric(df['Entrance Test Score'], errors='coerce')
df = df.dropna(subset=['Entrance Test Score'])

Q1 = df['Entrance Test Score'].quantile(0.25)
Q3 = df['Entrance Test Score'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df = df[(df['Entrance Test Score'] >= lower_bound) & (df['Entrance Test Score'] <= upper_bound)]


plt.figure(figsize=(6, 5))
sns.boxplot(y=df['Entrance Test Score'])
plt.show()

print("Missing Values:", df['Study Hours/Week'].isnull().sum())
mean_value = df['Study Hours/Week'].mean()
df['Study Hours/Week'].fillna(mean_value, inplace=True)

print("Missing Values:", df['High school GPA'].isnull().sum())
mean_value = df['High school GPA'].mean()
df['High school GPA'].fillna(mean_value, inplace=True)

print("Missing Values:", df['Distance (km)'].isnull().sum())
mean_value = df['Distance (km)'].mean()
df['Distance (km)'].fillna(mean_value, inplace=True)

df['Internet (Yes/No)']=LabelEncoder().fit_transform(df['Internet (Yes/No)'])
df['Final Year Result']=LabelEncoder().fit_transform(df['Final Year Result'])

x = df.drop(columns=['Final Year Result', 'Parental Income'], errors='ignore')
print(x)

y=df['Final Year Result']
print(y)

x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(x_train)
X_test = scaler.transform(x_test)

model = LogisticRegression(multi_class='ovr')
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

comparison_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(comparison_df.head(10))