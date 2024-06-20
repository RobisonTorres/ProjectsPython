import appStock

def main():

    # This function creates a menu.
    while True:
        menuOptions = [
            '1. Add new product',
            '2. Update a product',
            '3. Show all products',
            '4. Delete a product',
            '5. Exit the program']
        lineBase = 56 * '*'

        print(lineBase)
        print('Menu - Stock'.center(56))
        print(lineBase)
        for item in menuOptions:
            space = len(lineBase) - len(item)
            print(f'{"*" : <18}{item: ^8}{"*" : >{space - 18}} ')
        print(lineBase)
        option = input('Your option: ')
        
        if option == '1':
            appStock.add()
        elif option == '2':
            appStock.update()
        elif option == '3':
            print(lineBase)
            appStock.read()
            input('\nPress Enter to continue...')
        elif option == '4':
            appStock.delete()
        elif option == '5':
            print('Exit\n')
            break
        else:
            print('Wrong option.')      

main()