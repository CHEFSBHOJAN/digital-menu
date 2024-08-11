
import pandas as pd
import json

def extract_data_from_sheet(sheet):
    category_name = sheet.iloc[0, 2]  # Category name from C2 cell
    titles = sheet.iloc[2:, 2]  # Titles from C3 downwards
    prices = sheet.iloc[2:, 4]  # Prices from E3 downwards
    subcategories = sheet.iloc[2:, 5]  # Subcategories from F3 downwards
    veg_nonveg = sheet.iloc[2:, 6]  # VEG/NONVEG from G3 downwards
    
    data = {}
    print(sheet.shape)

    
    for title, price, subcategory,veg_nonveg_value in zip(titles, prices, subcategories, veg_nonveg):
        if pd.notna(title) and pd.notna(price) and pd.notna(subcategory):
            if subcategory not in data:
                data[subcategory] = []
                srum = 1
            item = {
                "srno": srum,
                "name": title,
                "price": price,
                "veg_nonveg": veg_nonveg_value
            }
            srum = srum + 1
            data[subcategory].append(item)
    
    return {"category": category_name, "subcategory": data}

def create_menu_json(excel_file):
    xls = pd.ExcelFile(excel_file)
    menu_data = []
    
    for sheet_name in xls.sheet_names:
        sheet = pd.read_excel(xls, sheet_name)
        category_data = extract_data_from_sheet(sheet)
        menu_data.append(category_data)
    
    with open('menu.json', 'w') as json_file:
        json.dump(menu_data, json_file, indent=4)

if __name__ == "__main__":
    excel_file = r"C:\Users\HP\OneDrive\Desktop\CLICKBATE_Developments\assets\margaomenu.xlsx"
    create_menu_json(excel_file)
