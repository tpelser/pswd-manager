from tkinter import ttk
import tkinter as tk
from utils.pwd_generator import generate_password
from utils.encryption import encrypt_password
from database.db import add_password_data
from gui.pwd_gen import prompt_password_generation_options
from gui.functions import get_salt
from tkinter import messagebox
from utils.clipboard import copy_to_clipboard

# add an entry Window
def add_entry(root, verified_master_password):
    def on_add_entry_submit(event=None):
        website = website_entry.get()
        email = email_entry.get()
        username = username_entry.get()
        password = password_entry.get()

        if not password:
            length, allow_numbers, allow_special_chars = prompt_password_generation_options(root)
            password = generate_password(length=length, allow_numbers=allow_numbers, allow_special_chars=allow_special_chars)
        
        salt = get_salt()
        encrypted_password = encrypt_password(password, verified_master_password, salt)
        add_password_data(website, email, username, encrypted_password)

        copy_to_clipboard(password)

        messagebox.showinfo("Success", "Password stored and copied to clipboard.") 
        add_entry_window.destroy()

    add_entry_window = tk.Toplevel(root)
    add_entry_window.title("Add an Entry")
    add_entry_window.geometry("600x400")
    add_entry_window.bind('<Return>', on_add_entry_submit)

    ttk.Label(add_entry_window, text="Website URL:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
    website_entry = ttk.Entry(add_entry_window)
    website_entry.grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(add_entry_window, text="Email:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
    email_entry = ttk.Entry(add_entry_window)
    email_entry.grid(row=1, column=1, padx=10, pady=10)

    ttk.Label(add_entry_window, text="Username (optional):").grid(row=2, column=0, padx=10, pady=10, sticky='e')
    username_entry = ttk.Entry(add_entry_window)
    username_entry.grid(row=2, column=1, padx=10, pady=10)

    ttk.Label(add_entry_window, text="Password (leave empty to generate):").grid(row=3, column=0, padx=10, pady=10, sticky='e')
    password_entry = ttk.Entry(add_entry_window)
    password_entry.grid(row=3, column=1, padx=10, pady=10)

    submit_button = ttk.Button(add_entry_window, text="Submit", command=on_add_entry_submit)
    submit_button.grid(row=4, column=1, padx=10, pady=10)