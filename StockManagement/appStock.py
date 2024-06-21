import openSave
file = openSave.open_file()

def checkInput(function, product):

    # This function checks if the user's input is valid.
    try:
        newProductPrice = float(input(f"Enter the {product}'s price: ").replace(' ', ''))
        newProductQuantity = int(input(f"Enter the {product}'s quantity in stock: ").replace(' ', ''))
    
        if newProductPrice > 0 and newProductQuantity >= 0: 
            file[product.capitalize()] = [round(newProductPrice, 2), newProductQuantity]
            openSave.save_file(file)
            print(f'The stock has been updated - {product}.')
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
        nameProduct = input(f'Enter the product you would like to update: ').capitalize()

    if nameProduct not in list(file.keys()):
        print(f'{nameProduct} is not present in the stock.')
        mayAdd = input(f"Pres 'y' if you would like to add {nameProduct}: ").lower()
        if mayAdd == 'y':
            return add(nameProduct)
        else:
            return update()      
        
    checkInput(update, nameProduct)

def delete():

    # This function deletes product present in the stock.
    if len(file) == 0:
        print("Stock empty! There\'s nothing to delete.\n")
        return read()
    
    deleteProduct = input('Enter the product you would like to delete: ').capitalize()

    if deleteProduct not in list(file.keys()):
        print(f'{deleteProduct} is not present in the stock.')
        delete()
    else:
        del file[deleteProduct]
        openSave.save_file(file)
        print(f'{deleteProduct} has been deleted from the stock.')

def read():

    # This function reads all the products present in the stock.
    file = dict(sorted(openSave.open_file().items(),key=lambda x:str(x[0])))
    openSave.save_file(file) 
    print(f"{'Name' : <18}|{'Price' : ^18}|{'Quantity' : >18}") 
    for key, value in file.items():
        print(f'{key: <18}|{value[0]: ^18.2f}|{value[1]: >18}')