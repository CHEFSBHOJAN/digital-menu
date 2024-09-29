from flask import Flask, jsonify, redirect, render_template,request, url_for
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from pymongo import MongoClient
import json
import os

app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*")

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
WebMenu = db['WEBSITE_MENU']

@app.route('/')
def index():
    margao_menu = list(MargaoMenu.find())
    ponda_menu = list(PondaMenu.find())
    return render_template('index.html', margao_menu=margao_menu, ponda_menu=ponda_menu)

@app.route('/api/getmenuweb', methods=['GET'])
def getWebMenu():
    print("API /getmenuweb hit")

    # Handle preflight requests for CORS
    if request.method == 'OPTIONS':
        return jsonify({'status': 'success', 'message': 'CORS preflight request handled successfully'}), 200

    # Fetch dishes from WebMenu
    try:
        dishes = list(WebMenu.find({}, {'_id': 0}))  # Fetch all dishes without the `_id` field
        return render_template('WebMenu.html', dishes=dishes)  # Render WebMenu.html with dishes
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        print(error_message)
        return jsonify({'status': 'error', 'message': error_message}), 500  # Return error message

    
# WebMenu Routes

@app.route('/api/add_category_web', methods=['POST'])
def add_category_web():
    data = request.json
    category_name = data.get('categoryName')

    if not category_name:
        return jsonify({'error': 'Category name is required'}), 400

    try:
        # Check if the category already exists in WebMenu
        if WebMenu.find_one({'category': category_name}):
            return jsonify({'error': 'Category already exists'}), 400
        
        # Add the new category to WebMenu
        WebMenu.insert_one({
            'category': category_name,
            'subcategory': {}  # Initialize with an empty subcategory dictionary
        })

        socketio.emit('menu_update', {'menuType': 'web'})

        return jsonify({'status': 'success', 'message': 'Category added successfully'}), 200
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

@app.route('/api/add_subcategory_web', methods=['POST'])
def add_subcategory_web():
    data = request.json
    category_name = data.get('categoryName')
    subcategory_name = data.get('subcategoryName')

    if not category_name or not subcategory_name:
        return jsonify({'error': 'Both category name and subcategory name are required'}), 400

    try:
        # Check if the category exists in WebMenu
        category = WebMenu.find_one({'category': category_name})
        if not category:
            return jsonify({'error': 'Category does not exist'}), 400
        
        # Check if the subcategory already exists
        if subcategory_name in category['subcategory']:
            return jsonify({'error': 'Subcategory already exists'}), 400

        # Add the new subcategory
        WebMenu.update_one(
            {'category': category_name},
            {'$set': {f'subcategory.{subcategory_name}': []}}  # Initialize with an empty list
        )

        socketio.emit('menu_update', {'menuType': 'web'})

        return jsonify({'status': 'success', 'message': 'Subcategory added successfully'}), 200
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

@app.route('/api/update_category_name_web', methods=['POST'])
def update_category_name_web():
    data = request.json
    old_name = data['oldName']
    new_name = data['newName']

    try:
        WebMenu.update_one({'category': old_name}, {'$set': {'category': new_name}})

        socketio.emit('menu_update', {'menuType': 'web'})
        return jsonify({'status': 'success', 'message': 'Category name updated successfully'}), 200
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

@app.route('/api/update_subcategory_name_web', methods=['POST'])
def update_subcategory_name_web():
    data = request.json
    category_name = data['categoryName']
    old_subcategory_name = data['oldSubcategoryName']
    new_subcategory_name = data['newSubcategoryName']

    try:
        WebMenu.update_one(
            {'category': category_name, f'subcategory.{old_subcategory_name}': {'$exists': True}},
            {'$rename': {f'subcategory.{old_subcategory_name}': f'subcategory.{new_subcategory_name}'}}
        )

        socketio.emit('menu_update', {'menuType': 'web'})
        return jsonify({'status': 'success', 'message': 'Subcategory name updated successfully'}), 200
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500
    
@app.route('/api/update_imgurl_web', methods=['POST'])
def update_item_imgurl_web():
    data = request.json
    category_name = data['categoryName']
    subcategory_name = data['subcategoryName']
    item_name = data['itemName']
    new_imgurl_name = data['newImgUrl']
    
    print(data)

    try:
        WebMenu.update_one(
            {'category': category_name, f'subcategory.{subcategory_name}.name': item_name},
            {'$set': {f'subcategory.{subcategory_name}.$[elem].img': new_imgurl_name}},
            array_filters=[{'elem.name': item_name}]
        )

        socketio.emit('menu_update', {'menuType': 'web'})
        return jsonify({'status': 'success', 'message': 'Item image URL updated successfully'}), 200

    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500
    
@app.route('/api/update_description_web', methods=['POST'])
def update_item_description_web():
    data = request.json
    category_name = data['categoryName']
    subcategory_name = data['subcategoryName']
    item_name = data['itemName']
    new_description = data['newDescription']
    
    print(data)

    try:
        WebMenu.update_one(
            {'category': category_name, f'subcategory.{subcategory_name}.name': item_name},
            {'$set': {f'subcategory.{subcategory_name}.$[elem].description': new_description}},
            array_filters=[{'elem.name': item_name}]
        )

        socketio.emit('menu_update', {'menuType': 'web'})
        return jsonify({'status': 'success', 'message': 'Item description updated successfully'}), 200
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

@app.route('/api/update_genre_web', methods=['POST'])
def update_item_genre_web():
    data = request.json
    category_name = data['categoryName']
    subcategory_name = data['subcategoryName']
    item_name = data['itemName']
    new_genre = data['newGenre']
    
    print(data)

    try:
        WebMenu.update_one(
            {'category': category_name, f'subcategory.{subcategory_name}.name': item_name},
            {'$set': {f'subcategory.{subcategory_name}.$[elem].genre': new_genre}},
            array_filters=[{'elem.name': item_name}]
        )

        socketio.emit('menu_update', {'menuType': 'web'})
        return jsonify({'status': 'success', 'message': 'Item genre updated successfully'}), 200
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

@app.route('/api/add_item_web', methods=['POST'])
def add_item_web():
    data = request.json
    category_name = data.get('categoryName')
    subcategory_name = data.get('subcategoryName')
    new_item = data.get('newItem')

    try:
        WebMenu.update_one(
            {'category': category_name},
            {'$push': {f'subcategory.{subcategory_name}': new_item}}
        )

        socketio.emit('menu_update', {'menuType': 'web'})
        return jsonify({'status': 'success', 'message': 'Item added successfully'}), 200
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

@app.route('/api/delete_item_web', methods=['POST'])
def delete_item_web():
    data = request.json
    category_name = data.get('categoryName')
    subcategory_name = data.get('subcategoryName')
    item_name = data.get('itemName')

    try:
        result = WebMenu.update_one(
            {
                'category': category_name,
                f'subcategory.{subcategory_name}.name': item_name
            },
            {
                '$pull': {f'subcategory.{subcategory_name}': {'name': item_name}}
            }
        )
        
        if result.modified_count > 0:
            socketio.emit('menu_update', {'menuType': 'web'})
            return jsonify({'status': 'success', 'message': 'Item deleted successfully'}), 200
        else:
            return jsonify({'status': 'failure', 'message': 'Item not found'}), 404
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500


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
    
@app.route('/api/add_category', methods=['POST'])
def add_category():
    data = request.json
    category_name = data.get('categoryName')
    menu_type = data.get('menuType')

    menu_collection = MargaoMenu if menu_type == 'margao' else WebMenu if menu_type == 'web' else PondaMenu

    if not category_name:
        return jsonify({'error': 'Category name is required'}), 400

    try:
        # Check if the category already exists
        if menu_collection.find_one({'category': category_name}):
            return jsonify({'error': 'Category already exists'}), 400
        
        # Add the new category
        menu_collection.insert_one({
            'category': category_name,
            'subcategory': {}  # Initialize with an empty subcategory dictionary
        })
        
        socketio.emit('menu_update', {'menuType': menu_type})

        return jsonify({'status': 'success', 'message': 'Category added successfully'}), 200
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

@app.route('/api/add_subcategory', methods=['POST'])
def add_subcategory():
    data = request.json
    category_name = data.get('categoryName')
    subcategory_name = data.get('subcategoryName')
    menu_type = data.get('menuType')

    menu_collection = MargaoMenu if menu_type == 'margao' else WebMenu if menu_type == 'web' else PondaMenu

    if not category_name or not subcategory_name:
        return jsonify({'error': 'Both category name and subcategory name are required'}), 400

    try:
        # Check if the category exists
        category = menu_collection.find_one({'category': category_name})
        if not category:
            return jsonify({'error': 'Category does not exist'}), 400
        
        # Check if the subcategory already exists
        if subcategory_name in category['subcategory']:
            return jsonify({'error': 'Subcategory already exists'}), 400

        # Add the new subcategory
        menu_collection.update_one(
            {'category': category_name},
            {'$set': {f'subcategory.{subcategory_name}': []}}  # Initialize with an empty list
        )

        socketio.emit('menu_update', {'menuType': menu_type})

        return jsonify({'status': 'success', 'message': 'Subcategory added successfully'}), 200
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500
    
@app.route('/api/update_category_name', methods=['POST'])
def update_category_name():
    data = request.json
    old_name = data['oldName']
    new_name = data['newName']
    menu_type = data['menuType']

    menu_collection = MargaoMenu if menu_type == 'margao' else WebMenu if menu_type == 'web' else PondaMenu

    try:
        menu_collection.update_one({'category': old_name}, {'$set': {'category': new_name}})

        socketio.emit('menu_update', {'menuType': menu_type})
        return jsonify({'status': 'success', 'message': 'Category name updated successfully'}), 200
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

@app.route('/api/update_subcategory_name', methods=['POST'])
def update_subcategory_name():
    data = request.json
    category_name = data['categoryName']
    old_subcategory_name = data['oldSubcategoryName']
    new_subcategory_name = data['newSubcategoryName']
    menu_type = data['menuType']

    menu_collection = MargaoMenu if menu_type == 'margao' else PondaMenu

    try:
        menu_collection.update_one(
            {'category': category_name, f'subcategory.{old_subcategory_name}': {'$exists': True}},
            {'$rename': {f'subcategory.{old_subcategory_name}': f'subcategory.{new_subcategory_name}'}}
        )

        socketio.emit('menu_update', {'menuType': menu_type})
        return jsonify({'status': 'success', 'message': 'Subcategory name updated successfully'}), 200
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

@app.route('/api/update_item_name', methods=['POST'])
def update_item_name():
    data = request.json
    category_name = data['categoryName']
    subcategory_name = data['subcategoryName']
    old_item_name = data['oldItemName']
    new_item_name = data['newItemName']
    menu_type = data['menuType']

    menu_collection = MargaoMenu if menu_type == 'margao' else WebMenu if menu_type == 'web' else PondaMenu

    try:
        menu_collection.update_one(
            {'category': category_name, f'subcategory.{subcategory_name}.name': old_item_name},
            {'$set': {f'subcategory.{subcategory_name}.$[elem].name': new_item_name}},
            array_filters=[{'elem.name': old_item_name}]
        )

        socketio.emit('menu_update', {'menuType': menu_type})
        return jsonify({'status': 'success', 'message': 'Item name updated successfully'}), 200
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

@app.route('/api/update_item_price', methods=['POST'])
def update_item_price():
    data = request.json
    category_name = data['categoryName']
    subcategory_name = data['subcategoryName']
    item_name = data['itemName']
    new_price = data['newPrice']
    menu_type = data['menuType']

    menu_collection = MargaoMenu if menu_type == 'margao' else WebMenu if menu_type == 'web' else PondaMenu

    try:
        menu_collection.update_one(
            {'category': category_name, f'subcategory.{subcategory_name}.name': item_name},
            {'$set': {f'subcategory.{subcategory_name}.$[elem].price': new_price}},
            array_filters=[{'elem.name': item_name}]
        )

        socketio.emit('menu_update', {'menuType': menu_type})
        return jsonify({'status': 'success', 'message': 'Item price updated successfully'}), 200
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

@app.route('/api/update_item_type', methods=['POST'])
def update_item_type():
    data = request.json
    category_name = data['categoryName']
    subcategory_name = data['subcategoryName']
    item_name = data['itemName']
    new_type = data['newType']
    menu_type = data['menuType']

    menu_collection = MargaoMenu if menu_type == 'margao' else WebMenu if menu_type == 'web' else PondaMenu

    try:
        menu_collection.update_one(
            {'category': category_name, f'subcategory.{subcategory_name}.name': item_name},
            {'$set': {f'subcategory.{subcategory_name}.$[elem].veg_nonveg': new_type}},
            array_filters=[{'elem.name': item_name}]
        )

        socketio.emit('menu_update', {'menuType': menu_type})
        return jsonify({'status': 'success', 'message': 'Item type updated successfully'}), 200
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500
    
@app.route('/api/add_item', methods=['POST'])
def add_item():
    data = request.json
    category_name = data.get('categoryName')
    subcategory_name = data.get('subcategoryName')
    new_item = data.get('newItem')
    menu_type = data.get('menuType')

    menu_collection = MargaoMenu if menu_type == 'margao' else WebMenu if menu_type == 'web' else PondaMenu

    try:
        menu_collection.update_one(
            {'category': category_name},
            {'$push': {f'subcategory.{subcategory_name}': new_item}}
        )

        socketio.emit('menu_update', {'menuType': menu_type})
        return jsonify({'status': 'success', 'message': 'Item added successfully'}), 200
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

@app.route('/api/delete_item', methods=['POST'])
def delete_item():
    data = request.json
    category_name = data.get('categoryName')
    subcategory_name = data.get('subcategoryName')
    item_name = data.get('itemName')
    menu_type = data.get('menuType')

    menu_collection = MargaoMenu if menu_type == 'margao' else WebMenu if menu_type == 'web' else PondaMenu

    try:
        result = menu_collection.update_one(
            {
                'category': category_name,
                f'subcategory.{subcategory_name}.name': item_name
            },
            {
                '$pull': {f'subcategory.{subcategory_name}': {'name': item_name}}
            }
        )
        
        # Check if any document was modified
        if result.modified_count > 0:

            socketio.emit('menu_update', {'menuType': menu_type})
            return jsonify({'status': 'success', 'message': 'Item deleted successfully'}), 200
        else:
            return jsonify({'status': 'failure', 'message': 'Item not found'}), 404
            
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500


@app.route('/api/delete_category', methods=['POST'])
def delete_category():
    data = request.json
    category_name = data['categoryName']
    menu_type = data['menuType']

    menu_collection = MargaoMenu if menu_type == 'margao' else WebMenu if menu_type == 'web' else PondaMenu

    try:
        menu_collection.delete_one({'category': category_name})

        socketio.emit('menu_update', {'menuType': menu_type})
        return jsonify({'status': 'success', 'message': 'Category deleted successfully'}), 200
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

@app.route('/api/delete_subcategory', methods=['POST'])
def delete_subcategory():
    data = request.json
    category_name = data['categoryName']
    subcategory_name = data['subcategoryName']
    menu_type = data['menuType']

    menu_collection = MargaoMenu if menu_type == 'margao' else WebMenu if menu_type == 'web' else PondaMenu

    try:
        menu_collection.update_one(
            {'category': category_name},
            {'$unset': {f'subcategory.{subcategory_name}': ""}}
        )

        socketio.emit('menu_update', {'menuType': menu_type})
        return jsonify({'status': 'success', 'message': 'Subcategory deleted successfully'}), 200
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)