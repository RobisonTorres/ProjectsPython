# Stock Management System

## Introduction

This project provides a Stock Management System, enabling users to perform CRUD operations on stock items.

## Features

- **appStockSqk.py**: This script contains all the main application's functions.

    - **add**: Adds new products to the stock.
    - **update**: Updates existing products in the stock.
    - **delete**: Removes products from the stock.
    - **read**: Retrieves all products currently in the stock.

- **connectionSql.py**: Establishes the connection between Python and SQL Server.

## Prerequisites

- Python
- SQL Server
- Required Python packages: pypyodbc

## Usage Instructions

To use this repository, follow these steps:

1. Execute the following queries on your SQL Server:
   - Create the database named Stock:
     ```sql
     CREATE DATABASE Stock;
     ```
   - Create the table named Products:
     ```sql
     CREATE TABLE Products (
         Name nvarchar(50),
         Price Decimal(10, 2),
         Quantity int,
         CONSTRAINT InputUser CHECK (Price > 0 AND Quantity >= 0)
     );
     ```

2. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/RobisonTorres/ProjectsPython.git

3. Install required Python packages.

4. Navigate to the directory.

    ```bash
    cd ProjectsPython/StockManagementSql.

5. Execute the appStockSql.py.

## Example

After running the appStockSql.py you will be able to access the app's menu:

```
********************************************************
                      Menu - Stock
********************************************************
*                 1. Add new product                   * 
*                 2. Update a product                  * 
*                 3. Show all products                 * 
*                 4. Delete a product                  * 
*                 5. Exit the program                  * 
********************************************************
Your option: 3
Name              |      Price       |          Quantity
________________________________________________________
Headphones        |      69.50       |                10
Mouse             |      19.50       |                20
Pc                |      299.99      |                 5
Tv                |      499.99      |                 3

Press enter to continue...
```