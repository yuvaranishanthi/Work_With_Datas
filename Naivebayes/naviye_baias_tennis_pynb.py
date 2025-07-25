# -*- coding: utf-8 -*-
"""Naviye baias_tennis.pynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Djnt9QwhXPgbtnYDMi6ylEtPTZ4SkKKg
"""

from google.colab import files
uploaded=files.upload()



from sklearn.naive_bayes import CategoricalNB, MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

df=pd.read_csv('play_tennis_dataset.csv')

weather=df['Outlook']
play=df['Play']

le_weather = LabelEncoder()
le_play = LabelEncoder()

X=le_weather.fit_transform(weather).reshape(-1,1)
Y=le_play.fit_transform(play)

print(X)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.2)

model=CategoricalNB()
model.fit(X_train,y_train)

from sklearn.metrics import accuracy_score,classification_report
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("Classification Report:\n", classification_report(y_test, y_pred))