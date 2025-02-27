from flask import Flask, request, jsonify
from flask_cors import CORS  # To handle CORS easily
import util
import os  # To access environment variables

app = Flask(__name__)
CORS(app)  # Enable CORS

# Fetch BACKEND_URL from environment variable (use default if not set)
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:5000")

@app.route('/api/get_location_names', methods=['GET'])
def get_location_names():
    # Provide the locations to the frontend
    response = jsonify({
        'locations': util.get_location_names()
    })
    return response

@app.route('/api/predict_home_price', methods=['POST'])
def predict_home_price():
    # Get POST data
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    # Call the util function to get the price
    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
    
    # Send the estimated price back in the response
    response = jsonify({
        'estimated_price': estimated_price
    })
    return response

if __name__ == "__main__":
    print(f"Starting Python Flask Server For Home Price Prediction at {BACKEND_URL}...")
    util.load_saved_artifacts()  # Load pre-trained models and data
    app.run(debug=True)  # Flask will run on http://127.0.0.1:5000 by default
