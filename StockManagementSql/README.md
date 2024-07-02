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

- **flaskIntegration.py**: Makes the integration between Backend and Frontend.

## Prerequisites

- Python
- SQL Server
- Required Python packages: pypyodbc, flask, render_template, request

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

5. Execute the flaskIntegration.py.

## Example

After running the flaskIntegration.py, and clicking on the url link you will be able to access the app's menu on your browser:

<br>

<p align = "center"><img src = "https://github.com/RobisonTorres/ProjectsPython/assets/69907756/5f117bcd-ce09-4603-b46b-5f534fc980fe"></p>