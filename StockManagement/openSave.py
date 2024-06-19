import json

def open_file():
     
     # This function opens and loads json files.
    file = open('stockProducts.json')
    products = json.load(file)
    return products


def save_file(x):
    
    # This function saves the updated results.
    with open('stockProducts.json', 'w') as file:
        json.dump(x, file, indent = 2)
