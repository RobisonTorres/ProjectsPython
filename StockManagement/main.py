import appStock

def main():

    # This function creates a menu.
    while True:
        listOperation = ['Press 1 to add new product.', 'Press 2 to update a product.',
                         'Press 3 to show all products.', 'Press 4 to exit.']
        lineBase = 47 * '*'
        print('Menu - Stock'.center(47))
        
        print(lineBase)
        for item in listOperation:
            space = len(lineBase) - len(item) - 12
            print(f'*         {item}{space * " "} *')
        print(lineBase)

        option = input('Your option: ')
        if option == '1':
            print(lineBase)
            appStock.add()
        elif option == '2':
            print(lineBase)
            appStock.update()
        elif option == '3':
            print(lineBase)
            appStock.read()
            print(lineBase)
        elif option == '4':
            print('Exit\n')
            break
        else:
            print('Wrong option.')
        print()

main()