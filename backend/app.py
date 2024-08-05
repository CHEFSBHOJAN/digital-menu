from flask import Flask, jsonify,request
from flask_cors import CORS
import json
import os

app = Flask(__name__)

CORS(app, supports_credentials=True, allow_headers="*", origins="*", methods=["OPTIONS", "POST","GET"])
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)


@app.route('/api/getmenumargao', methods=['GET'])
def MargaoMenu():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'success', 'message': 'CORS preflight request handled successfully'}), 200
    
    try:
        menu_file_path = os.path.join(os.path.dirname(__file__), 'margaomenu.json')
        with open(menu_file_path, 'r') as file:
            dishes = json.load(file)
        return jsonify({'dishes': dishes}), 200
    except FileNotFoundError:
        error_message = "menu.json file not found"
        print(error_message)
        return jsonify({'error': error_message}), 500
    except json.JSONDecodeError:
        error_message = "Error decoding JSON from menu.json"
        print(error_message)
        return jsonify({'error': error_message}), 500
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        print(error_message)
        return jsonify({'error': error_message}), 500
    
@app.route('/api/getmenuponda', methods=['GET'])
def PondaMenu():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'success', 'message': 'CORS preflight request handled successfully'}), 200
    
    try:
        menu_file_path = os.path.join(os.path.dirname(__file__), 'pondamenu.json')
        with open(menu_file_path, 'r') as file:
            dishes = json.load(file)
        return jsonify({'dishes': dishes}), 200
    except FileNotFoundError:
        error_message = "menu.json file not found"
        print(error_message)
        return jsonify({'error': error_message}), 500
    except json.JSONDecodeError:
        error_message = "Error decoding JSON from menu.json"
        print(error_message)
        return jsonify({'error': error_message}), 500
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        print(error_message)
        return jsonify({'error': error_message}), 500

