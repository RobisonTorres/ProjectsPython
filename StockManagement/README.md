# Stock Management System

## Intro

This project aims to provide a Stock Management System using Python, allowing users to perform CRUD operations on stock items.

## Features 

 - ```appStock.py``` - This script gathers all the app's functions.
 Functions present in this file are:
  * checkInput - This function checks if the user's input is valid.
  * add - This function adds new products to the stock.
  * update - This function updates the products present in the stock.
  * delete - This function deletes products present in the stock.
  * read - This function reads all the products present in the stock.

 - ```main.py``` - This function creates the app's menu and executes its functionalities.
 - ```OpenSave.py``` - This function opens and loads stockProducts.json file.
 - ```stockProducts.json``` - The file gathers all the stock information like name, price and quantity of each product.
 
## Prerequisites

- Python
- Required Python packages: `json`

## Usage Instructions

To use this repository, follow these steps:

1. Clone the repository to your local machine.

   ```bash
  git clone https://github.com/RobisonTorres/ProjectsPython.git  

2. Install required Python packages.

3. Navigate to the directory.

   ```bash
  cd ProjectsPython/StockManagement.

4. Execute the main.py.

## Example

After running the main.py you be able to access the app's menu:

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
********************************************************
Name              |      Price       |          Quantity
________________________________________________________
Headphones        |      40.00       |                20
Home audio        |      80.99       |                15
Laptop            |      200.00      |                10
Monitor           |      150.50      |                 6
Smartphone        |      70.00       |                40
Tablet            |      125.00      |                25

Press Enter to continue...
```