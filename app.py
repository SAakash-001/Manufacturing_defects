# app.py
from flask import Flask, request, jsonify
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score

app = Flask(__name__)

# Global variables for the model and data
model = None
data = None

def train_model(data):
    X = data[["Temperature", "Run_Time"]]
    y = data["Downtime_Flag"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred)
    }
    return clf, metrics

@app.route("/upload", methods=["POST"])
def upload_data():
    global data
    try:
        file = request.files["file"]
        data = pd.read_csv(file)
        required_columns = {"Machine_ID", "Temperature", "Run_Time", "Downtime_Flag"}
        if not required_columns.issubset(set(data.columns)):
            missing = required_columns - set(data.columns)
            return jsonify({"error": f"Missing columns: {', '.join(missing)}"}), 400
        return jsonify({"message": "Data uploaded successfully!", "columns": data.columns.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/train", methods=["POST"])
def train():
    global model, data
    if data is None:
        return jsonify({"error": "No data uploaded. Please upload data first."}), 400
    
    model, metrics = train_model(data)
    joblib.dump(model, "model.pkl")
    return jsonify({"message": "Model trained successfully!", "metrics": metrics})

@app.route("/predict", methods=["POST"])
def predict():
    global model
    if model is None:
        return jsonify({"error": "No model trained. Please train a model first."}), 400
    
    try:
        input_data = request.json
        if not input_data:
            return jsonify({"error": "Invalid JSON input. Please provide the data in JSON format."}), 400

        X_new = pd.DataFrame([input_data])
        prediction = model.predict(X_new)[0]
        confidence = max(model.predict_proba(X_new)[0])
        result = {
            "Downtime": "Yes" if prediction == 1 else "No",
            "Confidence": round(confidence, 2)
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == "__main__":
    app.run(debug=True)
