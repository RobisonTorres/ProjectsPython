import openSave
file = openSave.open_file()

def checkInput(function, product):

    # This function checks if the user's input is valid.
    try:
        newProductPrice = float(input(f"Enter the {product} price: ").replace(' ', ''))
        newProductQuantity = int(input(f"Enter the {product} quantity in stock: ").replace(' ', ''))
    
        if newProductPrice > 0 and newProductQuantity >= 0: 
            file[product.capitalize()] = [round(newProductPrice, 2), newProductQuantity]
            openSave.save_file(file)
            print(f'The stock is updated - {product}.')
        else:
            print(f'Please, enter a valid price and quantity for {product}.')
            function(product)
    except ValueError:
        print(f'Please, enter a valid price and quantity for {product}.')
        function(product)

def add(newProduct=False):

    # This function adds new products to the stock.
    if newProduct == False:
        newProduct = input(f"Please, enter the new product's name: ").capitalize()
        if newProduct.isspace() or not newProduct.isalpha():
            print(f'Please, enter a valid name for the new product.')
            return add()
    
    if newProduct in list(file.keys()):
        print(f'{newProduct} is already in the stock.')
        mayUpdated = input(f"Pres 'y' if you would like to update {newProduct}: ").lower()
        if mayUpdated == 'y':
            return update(newProduct)
        else:
            return add()

    checkInput(add, newProduct)

def update(nameProduct=False):

    # This function updates the products present in the stock.
    if nameProduct == False:
        nameProduct = input(f'Enter the one you would like to update: ').capitalize()

    if nameProduct not in list(file.keys()):
        print(f'{nameProduct} is not present in the stock.')
        mayAdd = input(f"Pres 'y' if you would like to add {nameProduct}: ").lower()
        if mayAdd == 'y':
            return add(nameProduct)
        else:
            return update()      
        
    checkInput(update, nameProduct)

def read():

    # This function reads all the products present in the stock.
    print(f"{'Name' : <15}|{'Price' : ^15}|{'Quantity' : >15}") 
    for key, value in file.items():
        print(f'{key: <15}|{value[0]: ^15}|{value[1]: >15}')