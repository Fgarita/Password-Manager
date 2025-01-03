from database import create_table, add_password, get_password, update_password, delete_password, record_exists
import os
from gui import create_gui

# Crear la tabla de contraseñas si no existe
create_table()


def menu():
    print("\nPassword Manager")
    print("1. Agregar Contraseña")
    print("2. Obtener Contraseña")
    print("3. Actualizar una contraseña existente")
    print("4. Eliminar una contraseña")
    print("5. Salir")


def add_new_password():
    website = input("Ingrese el nombre del sitio web: ")
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")
    add_password(website, username, password)
    print("Contraseña agregada con éxito.")


# Función para obtener una contraseña existente
def get_existing_password():
    website = input("Ingrese el nombre del sitio web: ")
    username = input("Ingrese su nombre de usuario: ")
    if not record_exists(website, username):
        print("No existe ningún registro para esa combinación.")
        return
    password = get_password(website, username)
    print(f"La contraseña para {website} y {username} es: {password}")

# Función para actualizar una contraseña


def update_existing_password():
    website = input("Ingrese el nombre del sitio web: ")
    username = input("Ingrese su nombre de usuario: ")
    if not record_exists(website, username):
        print("No existe ningún registro para esa combinación.")
        return
    new_password = input("Ingrese la nueva contraseña: ")
    update_password(website, username, new_password)
    print("Contraseña actualizada exitosamente.")

# Función para eliminar una contraseña


def delete_existing_password():
    website = input("Ingrese el nombre del sitio web: ")
    username = input("Ingrese su nombre de usuario: ")
    if not record_exists(website, username):
        print("No existe ningún registro para esa combinación.")
        return
    delete_password(website, username)
    print("Contraseña eliminada exitosamente.")


def run():
    while True:
        menu()
        choice = input("Seleccione una opción: ")
        if choice == "1":
            add_new_password()
        elif choice == "2":
            get_existing_password()
        elif choice == "3":
            update_existing_password()
        elif choice == "4":
            delete_existing_password()
        elif choice == "5":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    create_gui()
