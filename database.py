import sqlite3
from utils import encrypt_password, decrypt_password

# Función para conectar con la base de datos SQLite


def create_connection():
    connection = sqlite3.connect("passwords.db")
    return connection

# Función para crear la tabla de contraseñas si no existe


def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            website TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

# Función para agregar una contraseña a la base de datos


def add_password(website, username, password):
    encrypted_password = encrypt_password(password)
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO passwords (website, username, password)
        VALUES (?, ?, ?)
    """, (website, username, encrypted_password))
    connection.commit()
    connection.close()

# Función para obtener una contraseña de la base de datos


def get_password(website, username):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT password FROM passwords WHERE website = ? AND username = ?
    """, (website, username))
    result = cursor.fetchone()
    connection.close()
    if result:
        return decrypt_password(result[0])
    return None

# Actualizar una contraseña existente


def update_password(website, username, new_password):
    encrypted_password = encrypt_password(new_password)
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE passwords
        SET password = ?
        WHERE website = ? AND username = ?
    """, (encrypted_password, website, username))
    conn.commit()
    conn.close()

# Borrar una contraseña


def delete_password(website, username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM passwords WHERE website = ? AND username = ?",
                   (website, username))
    conn.commit()
    conn.close()

# Verificar si un registro existe


def record_exists(website, username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM passwords WHERE website = ? AND username = ?",
                   (website, username))
    result = cursor.fetchone()
    conn.close()
    return result is not None
