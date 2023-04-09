import tkinter as tk
from tkinter import ttk
import os 
from gui.functions import check_if_first_submit, on_first_time_submit, on_submit
from gui.add_entry import add_entry
from database.db import db_config

folder_path = "usr"
MASTER_PASSWORD_FILE = os.path.join(folder_path, "master_password_hash.txt")
DEVICE_SECRET_FILE = os.path.join(folder_path,"device_secret.txt")

def main():
    verified_master_password = None

    def on_master_password_submit(*args):
        nonlocal verified_master_password
        submitted_password = master_password_entry.get()
        if on_submit_function(submitted_password):
            verified_master_password = submitted_password
            master_password_prompt.destroy()

    # Create the main window
    root = tk.Tk()
    root.title("Password Manager")
    root.geometry("800x600")
    root.withdraw()

    # Set the color scheme
    bg_color = "#FFFFFF"  # White
    accent_color1 = "#FFA500"  # Orange
    accent_color2 = "#000080"  # Dark Blue

    # Style the app
    style = ttk.Style()
    style.configure(".", font=("Helvetica", 12), background=bg_color)
    style.configure("TLabel", foreground=accent_color2)
    style.configure("TButton", foreground=accent_color2)
    style.map("TButton", background=[("pressed", accent_color1), ("active", accent_color2)])

    # Create labels and buttons
    ttk.Label(root, text="Welcome to Password Manager", font=("Helvetica", 16, "bold")).pack(pady=20)
    
    add_entry_button = ttk.Button(root, text="Add an Entry", width=20, command=lambda: add_entry(root, verified_master_password))
    add_entry_button.pack(pady=10)

    retrieve_password_button = ttk.Button(root, text="Retrieve a Password", width=20)
    retrieve_password_button.pack(pady=10)

    quit_button = ttk.Button(root, text="Quit", width=20, command=root.destroy)
    quit_button.pack(pady=10)

    # Create a master password prompt window
    master_password_prompt = tk.Toplevel(root)
    master_password_prompt.title("Master Password Prompt")
    master_password_prompt.geometry("300x200")

    # check if first time running program
    first_time = check_if_first_submit()

    if first_time:
        ttk.Label(master_password_prompt, text="Create a master password: ").pack(pady=10)
        on_submit_function = on_first_time_submit
    else:
        ttk.Label(master_password_prompt, text="Enter your master password:").pack(pady=10)
        on_submit_function = on_submit

    master_password_entry = ttk.Entry(master_password_prompt, show="*")
    master_password_entry.pack(pady=10)
    master_password_entry.focus()


    submit_button = ttk.Button(master_password_prompt, text="Submit", command=on_master_password_submit)
    submit_button.pack(pady=10)
    master_password_prompt.bind('<Return>', on_master_password_submit)

    master_password_prompt.protocol("WM_DELETE_WINDOW", root.destroy)  # Close the app if the master password prompt is closed

    # Wait for the master password prompt to close
    root.wait_window(master_password_prompt)

    # show the main window after master_password_prompt is closed
    root.deiconify()

    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()