import os
from .hashing import hash_password, verify_password
from .pwd_generator import generate_password
from .clipboard import copy_to_clipboard

MASTER_PASSWORD_FILE = "master_password_hash.txt"
DEVICE_SECRET_FILE = "device_secret.txt"

def setup_master_key():
    if not os.path.exists(MASTER_PASSWORD_FILE):
        master_password = input("Welcome to the PWD Manager! Enter a new master password: ")
        password_hash = hash_password(master_password)

        with open(MASTER_PASSWORD_FILE, "wb") as f:
            f.write(password_hash.encode())

        # Generate and store the device secret
        device_secret = generate_password(length=64, allow_numbers=True, allow_special_chars=False)
        with open(DEVICE_SECRET_FILE, "w") as f:
            f.write(device_secret)

        # copy the master password to clipboard in case they forgot to write it down
        copy_to_clipboard(master_password)
        print("Master password saved and copied to clipboard. \n In case you haven't saved this somewhere yet, please paste the contents of your clipboard in a text file and save it in a secure location! \n DO NOT LOSE THIS PASSWORD!")

    return read_device_secret()

def read_device_secret():
    with open(DEVICE_SECRET_FILE, "r") as f:
        return f.read()
    
def verify_master_password(master_password):
    with open(MASTER_PASSWORD_FILE, "rb") as f:
        stored_hash = f.read()
    return verify_password(master_password, stored_hash)