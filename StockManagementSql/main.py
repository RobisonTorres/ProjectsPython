import appStockSql

def main():

    # This function creates the app's menu and executes its functionalities.
    while True:
        menuOptions = ['1. Add new product', '2. Update a product', '3. Show all products', '4. Delete a product', '5. Exit the program']
        lineBase = 56 * '*'
        print(lineBase + '\n' + 'Menu - Stock'.center(56) + '\n' + lineBase)
        for item in menuOptions:
            space = len(lineBase) - len(item)
            print(f'{"*" : <18}{item: ^8}{"*" : >{space - 18}} ')

        option = input(lineBase + '\nYour option: ')
        match option:
            case '1':
                appStockSql.add()
            case '2':
                appStockSql.update()
            case '3':
                appStockSql.read()
                print(input('Press enter to continue...'))
            case '4':
                appStockSql.delete()
            case '5':
                print('Exiting...\n')
                break
            case _:
                print('Wrong option.')      
main()