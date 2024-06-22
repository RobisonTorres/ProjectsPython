from connectionSql import connection

products = connection().cursor().execute('Select * From Products').fetchall()
products = [product[0] for product in products]

def add():

    # This function...
    
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
     
    productName = input('Name: ').capitalize()
    productPrice = float(input('Price: '))
    productQuantity = int(input('Quantity: '))

    executeSql(f"""
    INSERT INTO Products VALUES 
        ('{productName}', {productPrice}, {productQuantity});
    """)  
    print('News')

add()