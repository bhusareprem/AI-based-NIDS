import requests
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load a sample from the test dataset
df = pd.read_csv('UNSW_NB15_testing-set.csv')
df = df.drop(['id', 'attack_cat'], axis=1)
categorical_cols = ['proto', 'service', 'state']
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
df = df.fillna(0)

# Take the first row as a sample
sample = df.iloc[0].to_dict()
sample.pop('label')  # Remove the label for prediction

# Send request to FastAPI
url = 'http://127.0.0.1:8000/predict'
response = requests.post(url, json=sample)

# Print result
if response.status_code == 200:
    prediction = response.json()['prediction']
    print(f"Prediction: {prediction} ({'Normal' if prediction == 0 else 'Intrusion'})")
    print(f"Actual Label: {df.iloc[0]['label']}")
else:
    print(f"Error: {response.status_code} - {response.text}")