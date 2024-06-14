
# Diabetes Prediction Web Application

![Demo](demo.gif)

## Overview
This Flask web application predicts the likelihood of diabetes based on input features such as glucose level, blood pressure, BMI, etc. It utilizes a machine learning model trained on relevant medical data.

## Features
- **Prediction**: Users can input their health metrics and get an instant prediction.
- **User-friendly Interface**: Simple and intuitive design for easy navigation.
- **Feedback**: Provides actionable insights based on the prediction.
- **Scalable**: Designed to handle multiple users concurrently.

## Tech Stack
- **Backend**: Flask, Python
- **Machine Learning**: Scikit-learn
- **Data Handling**: Pandas
- **Data Preprocessing**: StandardScaler
- **Model**: Support Vector Machine (SVM)

## Installation
Follow these steps to run the application locally:

1. Clone the repository:
   ```
   https://github.com/Ragaroop-IITD/Diabetes-Prediction-Web-Application.git
   ```
   
2. Navigate into the project directory:
   ```
   cd Diabetes-Prediction-Web-Application
   ```

3. Install dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

4. Download the diabetes dataset (`diabetes.xls`) and place it in the project directory.

5. Run the Flask application:
   ```
   flask run
   ```

6. Open your web browser and go to `http://127.0.0.1:5000/` to view the application.

## Usage
- Enter the required health metrics.
- Click on the "Predict" button to see the prediction.
- The result will indicate the likelihood of having diabetes based on the input.

## Directory Structure
```
├── app.py                 # Flask application
├── diabetes.xls           # Dataset
├── requirements.txt       # Dependencies
├── static                 # CSS files
│   └──css
│     └── style.css
├── templates              # HTML templates
│   └── index.html
└── README.md              # Project documentation
```

## Implementation Details
- **Model Training**: The SVM model is trained using the diabetes dataset (`diabetes.xls`). The data is standardized using `StandardScaler` before fitting the model.
- **Prediction Endpoint**: POST request to `/predict` expects JSON input with health metrics. It returns a prediction indicating the presence or absence of diabetes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please feel free to fork the repository and submit pull requests with your changes.


