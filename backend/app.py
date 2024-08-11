from flask import Flask, jsonify,request
from flask_cors import CORS
from pymongo import MongoClient
import json
import os

app = Flask(__name__)

CORS(app, supports_credentials=True, allow_headers="*", origins="*", methods=["OPTIONS","GET"])
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

# MONGODB_URI = os.getenv('MONGODB_URI')
# if not MONGODB_URI:
#     raise ValueError("Missing MONGODB_URI environment variable")

client = MongoClient(
    'mongodb+srv://ChefsBhojan:usX7ZS8kPz4Pv@cluster0.eikei2d.mongodb.net/',
    connectTimeoutMS=30000, 
    socketTimeoutMS=None)
db = client['DIGITALMENU']
PondaMenu = db['CB_PONDAMENU']
MargaoMenu = db['CB_MARGAOMENU']

@app.route('/api/getmenumargao', methods=['GET'])
def getMargaoMenu():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'success', 'message': 'CORS preflight request handled successfully'}), 200

    try:
        dishes = list(MargaoMenu.find({}, {'_id': 0})) 
        return jsonify({'dishes': dishes}), 200
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        print(error_message)
        return jsonify({'error': error_message}), 500
    
@app.route('/api/getmenuponda', methods=['GET'])
def getPondaMenu():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'success', 'message': 'CORS preflight request handled successfully'}), 200

    try:
        dishes = list(PondaMenu.find({}, {'_id': 0})) 
        return jsonify({'dishes': dishes}), 200
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        print(error_message)
        return jsonify({'error': error_message}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)