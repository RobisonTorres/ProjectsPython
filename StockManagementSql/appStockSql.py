from connectionSql import connection
connection = connection()
cursor = connection.cursor() # Sql's cursor.

def inputUser():

    # This function asks user to input the product's price and quantity.
    newProductPrice = input(f"Enter the Product's price: ")
    newProductQuantity = input(f"Enter the Product's quantity in stock: ")
    return [newProductPrice, newProductQuantity]

def add(newProduct=False):

    # This function adds new products to the stock.
    if newProduct == False:
        newProduct = input(f"Please, enter the new product's name: ").replace(' ', '').capitalize()
        
    if newProduct in products:
        print(f'{newProduct} is already in the stock.')
        mayUpdated = input(f"Pres 'y' if you would like to update {newProduct}: ").lower()
        if mayUpdated == 'y':
            return update(newProduct)
        else:
            return add()
            
    priceQuantity = inputUser()    
    try:
        cursor.execute(f"""INSERT INTO Products VALUES ('{newProduct}', {float(priceQuantity[0])}, {int(priceQuantity[1])});""")  
        connection.commit()
        print(f'The stock has been updated - {newProduct}.')
    except ValueError:
        print(f'Please, enter a valid price and quantity for {newProduct}.')
        add(newProduct)

def update(updateProduct=False):

    # This function updates the products present in the stock.
    if updateProduct == False:
        updateProduct = input(f'Enter the product you would like to update: ').replace(' ', '').capitalize()

    if updateProduct not in products:
        print(f'{updateProduct} is not present in the stock.')
        mayAdd = input(f"Pres 'y' if you would like to add {updateProduct}: ").lower()
        if mayAdd == 'y':
            return add(updateProduct)
        else:
            return update()
        
    priceQuantity = inputUser()
    try:
        cursor.execute(f"""Update Products Set Price = {priceQuantity[0]}, Amount = {priceQuantity[1]} Where Name = '{updateProduct}';""")  
        connection.commit()
        print(f'The stock has been updated - {updateProduct}.')
    except ValueError:
        print(f'Please, enter a valid price and quantity for {updateProduct}.')
        update(updateProduct)

def delete():

    # This function deletes product present in the stock.
    if len(products) == 0:
        print("Stock empty! There\'s nothing to delete.\n")
        return read()
    
    deleteProduct = input('\nEnter the product you would like to delete: ').capitalize()
    if deleteProduct not in products:
        print(f'{deleteProduct} is not present in the stock.\n')
        read()
        print('You have this products in stock.')
        delete()
    else:
        cursor.execute(f"""Delete Products Where Name = '{deleteProduct}';""")  
        connection.commit() 
        print(f'{deleteProduct} has been deleted from the stock.')
    
def read():

    # This function reads all the products present in the stock.
    productsList = cursor.execute('Select * From Products Order By Name Asc;').fetchall()
    print(f"{'Name' : <18}|{'Price' : ^18}|{'Quantity' : >18}")
    print(56 * '_') 
    for product in productsList:
        print(f'{product[0]: <18}|{product[1]: ^18.2f}|{product[2]: >18}')

products = cursor.execute('Select * From Products').fetchall()
products = [p[0] for p in products] # Products present in the Products Table.