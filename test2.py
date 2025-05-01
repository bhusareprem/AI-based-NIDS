import requests
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('UNSW_NB15_testing-set.csv')
df = df.drop(['id', 'attack_cat'], axis=1)
categorical_cols = ['proto', 'service', 'state']
encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le  # Save encoders for reuse
df = df.fillna(0)

# Test the first sample (dur=0.000011, proto=udp, service=-, state=INT)
sample = df.iloc[0].to_dict()
actual_label = sample.pop('label')

url = 'http://127.0.0.1:8000/predict'
response = requests.post(url, json=sample)
if response.status_code == 200:
    prediction = response.json()['prediction']
    print(f"Prediction: {prediction} ({'Normal' if prediction == 0 else 'Intrusion'}) | Actual: {actual_label}")
    print("Sample sent:", sample)
else:
    print(f"Error: {response.status_code} - {response.text}")