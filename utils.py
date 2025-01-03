import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

# Función para cargar la clave de encriptación desde una variable de entorno


def load_key():
    # Intentamos obtener la clave de la variable de entorno "ENCRYPTION_KEY"
    key = os.getenv("ENCRYPTION_KEY")
    if key is None:
        raise ValueError(
            "La variable de entorno 'ENCRYPTION_KEY' no está definida.")
      # Aseguramos que la clave tenga una longitud de 16 bytes
    key = key[:16]  # Truncamos a 16 bytes si es más larga
    return key.encode()  # Aseguramos que la clave sea de tipo bytes


def encrypt_password(password):
    key = load_key()

    # Generamos un IV aleatorio
    iv = os.urandom(AES.block_size)  # 16 bytes para AES
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Ciframos la contraseña y le agregamos el padding necesario
    ciphered_data = cipher.encrypt(pad(password.encode(), AES.block_size))

    # Almacenamos el IV junto con el texto cifrado (primeros 16 bytes son el IV)
    encrypted_password = base64.b64encode(iv + ciphered_data)

    return encrypted_password

# Función para desencriptar una contraseña


def decrypt_password(encrypted_password):
    key = load_key()

    # Decodificamos el texto cifrado y extraemos el IV
    encrypted_data = base64.b64decode(encrypted_password)
    iv = encrypted_data[:AES.block_size]  # Primeros 16 bytes son el IV
    # El resto es la contraseña cifrada
    ciphered_data = encrypted_data[AES.block_size:]

    # Desciframos la contraseña
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_password = unpad(cipher.decrypt(
        ciphered_data), AES.block_size).decode()

    return decrypted_password
