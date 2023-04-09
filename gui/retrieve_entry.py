from utils.encryption import decrypt_password
from database.db import get_password_data_by_website
import tkinter as tk
from tkinter import ttk, messagebox
from gui.functions import get_salt
from utils.clipboard import copy_to_clipboard

def retrieve_entry(root, verified_master_password):
    def on_website_entry_submit():
        website = website_entry.get()
        password_data = get_password_data_by_website(website)

        if password_data:
            salt = get_salt()
            email_entry.config(state="normal")
            email_entry.delete(0, "end")
            email_entry.insert(0, password_data.email)
            email_entry.config(state="readonly")

            username_entry.config(state="normal")
            username_entry.delete(0, "end")
            username_entry.insert(0, password_data.username)
            username_entry.config(state="readonly")

            decrypted_password = decrypt_password(password_data.password_hash, verified_master_password, salt)
            password_entry.config(state="normal")
            password_entry.delete(0, "end")
            password_entry.insert(0, decrypted_password)
            password_entry.config(state="readonly")
            copy_to_clipboard(decrypted_password)
            notification_label.config(text="Password copied to clipboard!")
        else:
            messagebox.showerror("Error", "No entry found for the specified website.")

    retrieve_window = tk.Toplevel(root)
    retrieve_window.title("Retrieve Entry")
    retrieve_window.geometry("500x300")

    ttk.Label(retrieve_window, text="Website URL:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
    website_entry = ttk.Entry(retrieve_window)
    website_entry.grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(retrieve_window, text="Email:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
    email_entry = ttk.Entry(retrieve_window, state="readonly")
    email_entry.grid(row=1, column=1, padx=10, pady=10)

    ttk.Label(retrieve_window, text="Username:").grid(row=2, column=0, padx=10, pady=10, sticky='e')
    username_entry = ttk.Entry(retrieve_window, state="readonly")
    username_entry.grid(row=2, column=1, padx=10, pady=10)

    ttk.Label(retrieve_window, text="Password:").grid(row=3, column=0, padx=10, pady=10, sticky='e')
    password_entry = ttk.Entry(retrieve_window, state="readonly")
    password_entry.grid(row=3, column=1, padx=10, pady=10)

    submit_button = ttk.Button(retrieve_window, text="Submit", command=on_website_entry_submit)
    submit_button.grid(row=4, column=1, padx=10, pady=10)

    notification_label = ttk.Label(retrieve_window, text="")
    notification_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    retrieve_window.bind("<Return>", lambda event: on_website_entry_submit())