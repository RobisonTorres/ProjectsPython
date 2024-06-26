from flask import Flask, render_template, request
import appStockSql
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('stockInterface.html')

@app.route('/add', methods=["POST"])
def add():
    
    # This function adds items to the stock.
    productName = request.form['product_name'].replace(' ', '').capitalize()
    productPrice = request.form['product_price']
    productQuantity = request.form['product_quantity']
    result = appStockSql.add(productName, productPrice, productQuantity)
    return render_template('stockInterface.html', result_add = result)
    
@app.route('/update', methods=["POST"])
def update():

    # This function updates items in the stock.
    productName = request.form['product_name_update'].replace(' ', '').capitalize()
    productPrice = request.form['product_price_update']
    productQuantity = request.form['product_quantity_update']
    result = appStockSql.update(productName, productPrice, productQuantity)
    return render_template('stockInterface.html', result_update = result)
    
@app.route('/delete', methods=["POST"])
def delete():

    # This function deletes items from the stock.
    itemToDelete = request.form['delete'].replace(' ', '').capitalize()
    result = appStockSql.delete(itemToDelete)
    return render_template('stockInterface.html', result_delete = result)

@app.route('/show')
def show():

    # This function show all the items present in the stock.
    result = appStockSql.read()
    return render_template('stockInterface.html', showItem = result)

if __name__ == '__main__':
    app.run()