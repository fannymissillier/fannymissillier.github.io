from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from predict_fct import prediction_fct  

app = Flask(__name__)
CORS(app)  

@app.route('/predict', methods=['POST'])
def predict_route():
    data = request.get_json()
    name = data.get('name')   

    if not name:
        return jsonify({'error': 'Name input is required.'}), 400

    try:
        genres, gender, age, kindness, origin = prediction_fct(name)
        response = {
            'name': name,
            'genres': genres,
            'gender': gender.tolist(),
            'age': age.tolist(),
            'kindness': kindness.tolist(),
            'origin': origin.tolist()
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Use Heroku's dynamic port and ensure the app runs in production mode
    port = int(os.environ.get('PORT', 5000))  # Use Heroku's $PORT environment variable
    app.run(host='0.0.0.0', port=port, debug=True)  # Set host to '0.0.0.0' for external access

