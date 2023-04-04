import os
from .hashing import hash_password, verify_password
from .pwd_generator import generate_password
from .clipboard import copy_to_clipboard
import platform
import ctypes

folder_path = "usr"

def is_windows():
    return platform.system().lower() == "windows"

def set_read_only_unix(file_path):
    os.chmod(file_path, 0o444)

def set_read_only_windows(file_path):
    FILE_ATTRIBUTE_READONLY = 0x01
    ctypes.windll.kernel32.SetFileAttributesW(file_path, FILE_ATTRIBUTE_READONLY)

def set_read_only(file_path):
    if is_windows():
        set_read_only_windows(file_path)
    else:
        set_read_only_unix(file_path)

MASTER_PASSWORD_FILE = os.path.join(folder_path, "master_password_hash.txt")
DEVICE_SECRET_FILE = os.path.join(folder_path,"device_secret.txt")

def setup_master_key():
    if not os.path.exists(folder_path):
        if platform.system() == "Windows":
            os.makedirs(folder_path, exist_ok=True)
            FILE_ATTRIBUTE_HIDDEN = 0x02
            ctypes.windll.kernel32.SetFileAttributesW(folder_path, FILE_ATTRIBUTE_HIDDEN)
        else:
            os.makedirs(folder_path, exist_ok=True)

    master_password = input("Welcome to the PWD Manager! Enter a new master password: ")
    password_hash = hash_password(master_password)

    with open(MASTER_PASSWORD_FILE, "wb") as f:
        f.write(password_hash.encode())
    set_read_only(MASTER_PASSWORD_FILE)

    # Generate and store the device secret
    device_secret = generate_password(length=64, allow_numbers=True, allow_special_chars=False)
    with open(DEVICE_SECRET_FILE, "wb") as f:
        f.write(device_secret.encode())
    set_read_only(DEVICE_SECRET_FILE)

    # copy the master password to clipboard in case they forgot to write it down
    copy_to_clipboard(master_password)
    print("Master password saved and copied to clipboard. \n In case you haven't saved this somewhere yet, please paste the contents of your clipboard in a text file and save it in a secure location! \n DO NOT LOSE THIS PASSWORD!")

    return read_device_secret()

def read_device_secret():
    with open(DEVICE_SECRET_FILE, "rb") as f:
        return f.read()
    
def verify_master_password(master_password):
    with open(MASTER_PASSWORD_FILE, "rb") as f:
        stored_hash = f.read()
    return verify_password(master_password, stored_hash)