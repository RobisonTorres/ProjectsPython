import appStock

def main():

    # This function creates a menu.
    while True:
        menuOptions = [
            '1. Add new product',
            '2. Update a product',
            '3. Show all products',
            '4. Exit the program'
        ]
        lineBase = 47 * '*'

        print(lineBase)
        print('Menu - Stock'.center(47))
        print(lineBase)
        for item in menuOptions:
            space = len(lineBase) - len(item)
            print(f'{"*" : <15}{item: ^5}{"*" : >{space - 15}} ')
        print(lineBase)
        option = input('Your option: ')
        
        if option == '1':
            appStock.add()
        elif option == '2':
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
        
        input('Press Enter to continue...')

main()