import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

# Load the test dataset
test_df = pd.read_csv('UNSW_NB15_testing-set.csv')

# Preprocess the test data (same as training)
test_df = test_df.drop(['id', 'attack_cat'], axis=1)
categorical_cols = ['proto', 'service', 'state']
for col in categorical_cols:
    le = LabelEncoder()
    test_df[col] = le.fit_transform(test_df[col])
test_df = test_df.fillna(0)

# Separate features and target
X_test = test_df.drop('label', axis=1)
y_test = test_df['label']

# Load the trained model
model = joblib.load('nids_model.pkl')

# Predict
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Local Test Accuracy: {accuracy * 100:.2f}%")

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))