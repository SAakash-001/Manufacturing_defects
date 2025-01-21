# Predictive Analysis for Manufacturing Operations

This project provides a RESTful API for predictive analysis in manufacturing operations, focusing on predicting machine downtime or production defects. The API includes endpoints for uploading data, training a machine learning model, and making predictions based on input parameters.

## Features

- **Upload Endpoint (`/upload`)**: Accepts a CSV file containing manufacturing data.
- **Train Endpoint (`/train`)**: Trains a machine learning model using the uploaded data and returns performance metrics.
- **Predict Endpoint (`/predict`)**: Accepts JSON input and returns predictions (e.g., whether downtime will occur).

---

## Getting Started

### Prerequisites

1. **Python 3.7+**
2. Required Python libraries:
   - Flask
   - pandas
   - scikit-learn
   - joblib

Install dependencies using:
```bash
pip install flask pandas scikit-learn joblib
```

---

### Setup Instructions

1. Clone the repository or download the files.
2. Navigate to the project directory.
3. Run the Flask server:
   ```bash
   python app.py
   ```

---

### API Endpoints

#### 1. **Upload Data**
   - **URL**: `/upload`
   - **Method**: `POST`
   - **Description**: Upload a CSV file containing manufacturing data.
   - **Request Body**: Use `form-data` with a file key `file`.
   - **Sample Response**:
     ```json
     {
       "message": "Data uploaded successfully!",
       "columns": ["Machine_ID", "Temperature", "Run_Time", "Downtime_Flag"]
     }
     ```

#### 2. **Train Model**
   - **URL**: `/train`
   - **Method**: `POST`
   - **Description**: Train a machine learning model on the uploaded data.
   - **Sample Response**:
     ```json
     {
       "message": "Model trained successfully!",
       "metrics": {
         "accuracy": 0.9,
         "f1_score": 0.85
       }
     }
     ```

#### 3. **Predict**
   - **URL**: `/predict`
   - **Method**: `POST`
   - **Description**: Make a prediction based on input parameters.
   - **Request Body**: JSON with keys `Temperature` and `Run_Time`.
     ```json
     {
       "Temperature": 85,
       "Run_Time": 130
     }
     ```
   - **Sample Response**:
     ```json
     {
       "Downtime": "Yes",
       "Confidence": 0.85
     }
     ```

---

### Testing the API

1. Use **Postman** or `cURL` to test the endpoints:
   - **Upload**:
     ```bash
     curl -X POST -F "file=@sample_data.csv" http://127.0.0.1:5000/upload
     ```
   - **Train**:
     ```bash
     curl -X POST http://127.0.0.1:5000/train
     ```
   - **Predict**:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"Temperature": 85, "Run_Time": 130}' http://127.0.0.1:5000/predict
     ```

2. Ensure the CSV file (`sample_data.csv`) has the following format:
   ```csv
   Machine_ID,Temperature,Run_Time,Downtime_Flag
   1,70,120,0
   2,85,130,1
   3,75,125,0
   4,90,140,1
   5,80,135,0
   ```

---

### Folder Structure

```
project-directory/
│
├── app.py               # Main Flask application
├── sample_data.csv      # Example dataset
├── README.md            # Documentation
```

---

### Notes

- Ensure the server is running before testing endpoints.
- Modify the dataset or model as needed for specific manufacturing use cases.

---

### Future Improvements

- Add authentication for API endpoints.
- Enhance the model with more complex algorithms.
- Integrate real-time data streams for predictions.

---

### Author
Developed by Aakash Singh.

