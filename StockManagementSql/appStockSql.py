from connectionSql import *
connection = connection()
cursor = connection.cursor() # Sql's cursor.

def add(newProduct, newProductPrice, newProductQuantity):

    # This function adds new products to the stock.        
    if newProduct in allProduct():
        return f'{newProduct} is already in the stock.'
        
    try:
        cursor.execute(f"""INSERT INTO Products VALUES ('{newProduct}', {float(newProductPrice)}, {int(newProductQuantity)});""")  
        connection.commit()
        return f'The stock has been updated - {newProduct}.'
    except (ValueError, odbc.Error):
        return f'Error! Price must be greater than $ 0.0 and quantity greater or equals to 0.' 

def update(updateProduct, updateProductPrice, updateProductQuantity):

    # This function updates the products present in the stock.
    if updateProduct not in allProduct():
        return f'{updateProduct} is not present in the stock.'        
        
    try:
        cursor.execute(f"""Update Products Set Price = {float(updateProductPrice)}, Quantity = {int(updateProductQuantity)} Where Name = '{updateProduct}';""")  
        connection.commit()
        return f'The stock has been updated - {updateProduct}.'
    except (ValueError, odbc.Error):
        return f'Error! Price must be greater than $ 0 and quantity greater or equals to 0.'

def delete(deleteProduct):

    # This function deletes product present in the stock.   
    if deleteProduct not in allProduct():
        return f'{deleteProduct} is not present in the stock.\n'
        
    else:
        cursor.execute(f"""Delete Products Where Name = '{deleteProduct}';""")  
        connection.commit() 
        return f'{deleteProduct} has been deleted from the stock.'
    
def read():
    
    # This function reads all the products present in the stock.
    productsList = cursor.execute('Select * From Products Order By Name Asc;').fetchall()
    showProducts = []
    for product in productsList:
        showProducts.append([product[0], float(product[1]), int(product[2])])
    return showProducts

def allProduct():

    # This function retrieves all the products present in the Products Table.
    products = cursor.execute('Select * From Products').fetchall()
    return [p[0] for p in products]