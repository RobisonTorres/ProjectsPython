from connectionSql import connection
connection = connection()
cursor = connection.cursor()

# This files creates the Products table on the Stock database.
cursor.execute("""
    CREATE TABLE Products (
    Name nvarchar(50),
    Price Decimal (10, 2),
    Quantity int,
    CONSTRAINT InputUser 
        CHECK (
            Name NOT LIKE '%[^A-Za-z]%' 
            AND Price > 0 
            AND Quantity >= 0
            )
    );
    """)

connection.commit()