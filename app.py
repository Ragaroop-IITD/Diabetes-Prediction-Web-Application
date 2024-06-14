from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

app = Flask(__name__)

# Load and prepare the diabetes dataset
diabetes_dataset = pd.read_excel("./diabetes.xls")
X = diabetes_dataset.drop(columns="Outcome", axis=1)
Y = diabetes_dataset["Outcome"]

scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)
A_train, A_test, B_train, B_test = train_test_split(
    standardized_data, Y, test_size=0.2, stratify=Y, random_state=2
)

classifier = svm.SVC(kernel="linear")
classifier.fit(A_train, B_train)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json['input_data']
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    std_data = scaler.transform(input_data_reshaped)
    prediction = classifier.predict(std_data)

    result = "I'm really sorry to share this, but you have been diagnosed with diabetes." if prediction[0] == 1 else "Great news, You don't have diabetes!"
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)

