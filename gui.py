import tkinter as tk
from tkinter import ttk, messagebox
from database import add_password, get_password, update_password, delete_password, record_exists

# Funciones para manejar eventos


def add_password_gui():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if not website or not username or not password:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return
    add_password(website, username, password)
    messagebox.showinfo("Éxito", "Contraseña agregada exitosamente.")
    clear_entries()


def view_password_gui():
    website = website_entry.get()
    username = username_entry.get()
    if not record_exists(website, username):
        messagebox.showerror(
            "Error", "No existe ningún registro para esta combinación.")
        return
    password = get_password(website, username)
    messagebox.showinfo(
        "Contraseña", f"La contraseña para {website} es: {password}")
    clear_entries()


def update_password_gui():
    website = website_entry.get()
    username = username_entry.get()
    new_password = password_entry.get()
    if not website or not username or not new_password:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return
    if not record_exists(website, username):
        messagebox.showerror(
            "Error", "No existe ningún registro para esta combinación.")
        return
    update_password(website, username, new_password)
    messagebox.showinfo("Éxito", "Contraseña actualizada exitosamente.")
    clear_entries()


def delete_password_gui():
    website = website_entry.get()
    username = username_entry.get()
    if not record_exists(website, username):
        messagebox.showerror(
            "Error", "No existe ningún registro para esta combinación.")
        return
    delete_password(website, username)
    messagebox.showinfo("Éxito", "Contraseña eliminada exitosamente.")
    clear_entries()


def clear_entries():
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Crear ventana principal


def create_gui():
    global website_entry, username_entry, password_entry

    # Configuración de la ventana principal
    window = tk.Tk()
    window.title("Password Manager")
    window.geometry("400x200")
    window.resizable(False, False)
    window.eval('tk::PlaceWindow . center')  # Centrar ventana en pantalla

    # Frame principal con padding
    main_frame = ttk.Frame(window, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Etiqueta de título
    title_label = ttk.Label(
        main_frame, text="Gestor de Contraseñas", font=("Helvetica", 16, "bold"))
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Etiquetas y campos de entrada
    ttk.Label(main_frame, text="Sitio Web:").grid(
        row=1, column=0, padx=5, pady=5, sticky="e")
    website_entry = ttk.Entry(main_frame, width=30)
    website_entry.grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(main_frame, text="Usuario:").grid(
        row=2, column=0, padx=5, pady=5, sticky="e")
    username_entry = ttk.Entry(main_frame, width=30)
    username_entry.grid(row=2, column=1, padx=5, pady=5)

    ttk.Label(main_frame, text="Contraseña:").grid(
        row=3, column=0, padx=5, pady=5, sticky="e")
    password_entry = ttk.Entry(main_frame, width=30, show="*")
    password_entry.grid(row=3, column=1, padx=5, pady=5)

    # Botones
    button_frame = ttk.Frame(main_frame)
    button_frame.grid(row=4, column=0, columnspan=2, pady=10)

    ttk.Button(button_frame, text="Agregar", command=add_password_gui).grid(
        row=0, column=0, padx=5)
    ttk.Button(button_frame, text="Ver", command=view_password_gui).grid(
        row=0, column=1, padx=5)
    ttk.Button(button_frame, text="Actualizar",
               command=update_password_gui).grid(row=0, column=2, padx=5)
    ttk.Button(button_frame, text="Eliminar",
               command=delete_password_gui).grid(row=0, column=3, padx=5)

    # Iniciar ventana
    window.mainloop()
