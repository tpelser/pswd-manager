from utils.master_key import verify_master_password
from utils.hashing import hash_password, verify_password
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import platform
import os 
import ctypes
from utils.master_key import set_read_only, read_device_secret
from utils.pwd_generator import generate_password
from utils.clipboard import copy_to_clipboard

folder_path = "usr"
MASTER_PASSWORD_FILE = os.path.join(folder_path, "master_password_hash.txt")
DEVICE_SECRET_FILE = os.path.join(folder_path,"device_secret.txt")

def check_if_first_submit():
    folder_path = "usr"
    if not os.path.exists(folder_path):
        return True
    else:
        return False

def setup_master_key(master_password):
    if platform.system() == "Windows":
            os.makedirs(folder_path, exist_ok=True)
            FILE_ATTRIBUTE_HIDDEN = 0x02
            ctypes.windll.kernel32.SetFileAttributesW(folder_path, FILE_ATTRIBUTE_HIDDEN)
    else:
        os.makedirs(folder_path, exist_ok=True)
    password_hash = hash_password(master_password)
    with open(MASTER_PASSWORD_FILE, "wb") as f:
        f.write(password_hash.encode())
    set_read_only(MASTER_PASSWORD_FILE)

    # Generate and store the device secret
    device_secret = generate_password(length=64, allow_numbers=True, allow_special_chars=False)
    with open(DEVICE_SECRET_FILE, "wb") as f:
        f.write(device_secret.encode())
    set_read_only(DEVICE_SECRET_FILE)

def get_salt():
    with open(DEVICE_SECRET_FILE, "rb") as f:
        return f.read()