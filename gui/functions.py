from utils.master_key import verify_master_password
from utils.hashing import hash_password, verify_password
import tkinter as tk
from tkinter import messagebox, simpledialog
import platform
import os 
import ctypes
from utils.master_key import set_read_only
from utils.pwd_generator import generate_password
from database.db import db_config
from utils.clipboard import copy_to_clipboard

folder_path = "usr"
MASTER_PASSWORD_FILE = os.path.join(folder_path, "master_password_hash.txt")
DEVICE_SECRET_FILE = os.path.join(folder_path,"device_secret.txt")
MINIMUM_MASTER_PASSWORD_LENGTH = 4

# check if it is the first time opening the program
def check_if_first_submit():
    folder_path = "usr"
    if not os.path.exists(folder_path):
        return True
    else:
        return False

# set up the master key 
def setup_master_key(master_password):
    os.makedirs(folder_path, exist_ok=True)
    db_config()
    if platform.system() == "Windows":
            FILE_ATTRIBUTE_HIDDEN = 0x02
            ctypes.windll.kernel32.SetFileAttributesW(folder_path, FILE_ATTRIBUTE_HIDDEN)
    password_hash = hash_password(master_password)
    with open(MASTER_PASSWORD_FILE, "wb") as f:
        f.write(password_hash.encode())
    set_read_only(MASTER_PASSWORD_FILE)

    # Generate and store the device secret
    device_secret = generate_password(length=64, allow_numbers=True, allow_special_chars=False)
    with open(DEVICE_SECRET_FILE, "wb") as f:
        f.write(device_secret.encode())
    set_read_only(DEVICE_SECRET_FILE)

# read the device secret
def get_salt():
    with open(DEVICE_SECRET_FILE, "rb") as f:
        return f.read()

def on_submit(master_password):
    if verify_master_password(master_password):
        return True
    else:
        messagebox.showerror("Error", "Incorrect master password!")
        return False

# first time opening the program, create a new master password
def on_first_time_submit(master_password):
    if len(master_password) < MINIMUM_MASTER_PASSWORD_LENGTH:
        messagebox.showerror("Error", f"Master password must be at least {MINIMUM_MASTER_PASSWORD_LENGTH} characters long!")
        return False
    else:
        setup_master_key(master_password)
        copy_to_clipboard(master_password)
        messagebox.showinfo("Success", "Master password created and copied to clipboard. DO NOT LOSE THIS PASSWORD!")
        return True
    
# now create a prompt that the user has to confirm their password has been securely stored.
