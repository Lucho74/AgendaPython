from os import system

from .ContactView import ContactView
from .UserView import UserView
from Controllers.UserController import UserController

class MainMenu:

    def menu(self):
        while True:
            system("cls")
            print(" Bienvenido a la agenda de contactos ".center(50, "#"))
            print("1. Login de usuario")
            print("2. Registro de usuario")
            print("3. Listar Usuarios")
            print("4. Baja de usuario")
            print("5. Salir del programa")
            print("-" * 50)
            option = input("Ingrese una opcion: ")
            if option == "1" or option == "4":
                user_view = UserView()
                validation = user_view.login_menu(option)
                if validation[0] == True:
                    if option == "1":
                        user = validation[1]
                        ContactView(user).menu()
                    else:
                        user = validation[1]
                        user_controller = UserController()
                        user_controller.delete_user(user)
                else:
                    print(" Usuario o contraseña incorrecta ".center(50, "!"))
                    input(" Presione enter para continuar ".center(50, "!"))
            elif option == "2":
                user_view = UserView()
                validation = user_view.add_user_menu()
            elif option == "3":
                user_view = UserView()
                validation = user_view.list_users()
            elif option == "5":
                break
            else:
                print(" Opcion incorrecta ".center(50, "!"))
                input(" Presione enter para continuar ".center(50, "!"))


if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.menu()
