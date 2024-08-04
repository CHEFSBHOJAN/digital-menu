from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)

CORS(app, supports_credentials=True, allow_headers="*", origins="*", methods=["OPTIONS", "POST","GET"])
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

@app.route('/api/getmenu', methods=['GET']) 
def Menu():
    if request.method == 'OPTIONS':
        return jsonify({'status': 'success', 'message': 'CORS preflight request handled successfully'}), 200
    
    try:
        with open('Menu.json', 'r') as file:
            data = json.load(file)
            dishes = data.get('dishes', [])
        return jsonify(dishes)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

    
      