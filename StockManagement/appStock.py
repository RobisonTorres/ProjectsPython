import openSave

file = openSave.open_file()

def add(newProduct=False):

    # This function adds new products to the stock.
    products = list(file.keys())
    if newProduct == False:
        newProduct = input(f"Please, enter the new product's name: ").replace(' ', '').capitalize()
    
    if newProduct in products:
        print(f'{newProduct} is already in the stock.')
        mayUpdated = input(f"Pres 'y' if you would like to update {newProduct}: ").lower()
        if mayUpdated == 'y':
            return update(newProduct)
        else:
            return add()

    newProductPrice = float(input(f"Enter the {newProduct} price: ").replace(' ', ''))
    newProductQuantity = int(input(f"Enter the {newProduct} quantity in stock: ").replace(' ', ''))
    file[newProduct.capitalize()] = [newProductPrice, newProductQuantity]
    openSave.save_file(file)
    print(f'{newProduct} has been added to the stock.')

def update(nameProduct=False):

    # This function updates the products present in the stock.
    products = list(file.keys())
    if nameProduct == False:
        nameProduct = input(f'Enter the one you would like to update: ').capitalize()
    if nameProduct not in products:
        print(f'{nameProduct} is not present in the stock.')
        mayAdd = input(f"Pres 'y' if you would like to add {nameProduct}: ").lower()
        if mayAdd == 'y':
            return add(nameProduct)
        else:
            return update()      
        
    nameProductPrice = float(input(f'Enter the new price for {nameProduct}: ').replace(' ', ''))
    nameProductQuantity = int(input(f'Enter the new quantity for {nameProduct}: ').replace(' ', ''))
    file[nameProduct] = [nameProductPrice, nameProductQuantity]
    openSave.save_file(file)
    print(f'Product {nameProduct} has been updated.')

def read():

    # This function reads all the products present in the stock.
    print(f"{'Name' : <15}|{'Price' : ^15}|{'Quantity' : >15}") 
    for key, value in file.items():
        print(f'{key: <15}|{value[0]: ^15}|{value[1]: >15}')