import json
import os
import uuid

def generate_unique_id():
    """Generate a unique ID."""
    return str(uuid.uuid4())

def assign_ids_to_items(menu):
    """Assign unique IDs to each item in the menu."""
    for category in menu:
        if 'subcategory' in category:
            for subcategory, items in category['subcategory'].items():
                for item in items:
                    item['id'] = generate_unique_id()
    return menu

def main():
    input_file = os.path.join(os.path.dirname(__file__), 'pondamenu.json')
    output_file = os.path.join(os.path.dirname(__file__), 'pondamenu2.json')
    
    # Read the existing menu data from JSON file
    with open(input_file, 'r') as file:
        menu = json.load(file)
    
    # Assign unique IDs to each item
    updated_menu = assign_ids_to_items(menu)
    
    # Write the updated menu data to a new JSON file
    with open(output_file, 'w') as file:
        json.dump(updated_menu, file, indent=4)
    
    print(f"Updated menu saved to {output_file}")

if __name__ == "__main__":
    main()
