import pypyodbc as odbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'RobisonTorres\SQLEXPRESS'
DATABASE_NAME = 'Stock'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;"""

conn = odbc.connect(connection_string)
cursor = conn.cursor()

'''  
    Create
cursor.execute(
    """
    CREATE TABLE Products (
    Name nvarchar(50),
    Price Decimal (10, 2),
    Amount int
    )
    """
)
    Insert
cursor.execute( 
    """
    INSERT INTO Products (Name, Price, Amount)
    VALUES
    ('A', 17.85, 800),
    ('B', 21.22, 1200),
    ('C', 30.00, 200),
    ('D', 45.00, 350),
    ('e', 9.99, 150)
    """
)
    Update
cursor.execute(
    """
    Update Products
    Set Price = 85.99
    Where Name = '5'
    """
)
    Insert
cursor.execute(
    """
    Insert Into Products Values ('F', 200.00, 5);
    """
)

a = 0.99
cursor.execute(f"""
    Update Products
    Set Price = {a}
    Where Name = 'A'
    """
)

conn.commit()

products = cursor.execute('Select * From Products')

for item in products:
    print(f'{list(item)[0]} cost {list(item)[1]}, and it has {list(item)[2]} in stock\n')
'''

list = ['Apple', 'Bike', 'Science']
test = 'A'
print(test in list)