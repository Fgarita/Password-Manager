from database import create_table, add_password, get_password

# Crear la tabla de contraseñas si no existe
create_table()


def menu():
    print("\nPassword Manager")
    print("1. Agregar Contraseña")
    print("2. Obtener Contraseña")
    print("3. Salir")


def add_new_password():
    website = input("Ingrese el nombre del sitio web: ")
    username = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")
    add_password(website, username, password)
    print("Contraseña agregada con éxito.")


def get_existing_password():
    website = input("Ingrese el nombre del sitio web: ")
    username = input("Ingrese el nombre de usuario: ")
    password = get_password(website, username)
    if password:
        print(f"La contraseña para {website} es: {password}")
    else:
        print("No se encontró la contraseña.")


def run():
    while True:
        menu()
        choice = input("Seleccione una opción: ")
        if choice == "1":
            add_new_password()
        elif choice == "2":
            get_existing_password()
        elif choice == "3":
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    run()
