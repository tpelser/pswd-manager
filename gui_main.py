import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from utils.master_key import verify_master_password, setup_master_key, verify_master_password
import os 
from gui.functions import setup_master_key, get_salt, check_if_first_submit

folder_path = "usr"
MASTER_PASSWORD_FILE = os.path.join(folder_path, "master_password_hash.txt")
DEVICE_SECRET_FILE = os.path.join(folder_path,"device_secret.txt")

## function for prompt when starting the program
def on_submit(master_password_entry, root):
    master_password = master_password_entry.get()
    if verify_master_password(master_password):
        root.deiconify()
        master_password_entry.delete(0, 'end')
        master_password_prompt.withdraw()
    else:
        messagebox.showerror("Error", "Incorrect master password. Please try again.")

# function for prompt when starting program for the first time
def on_first_time_submit(master_password_entry, root):
    master_password = master_password_entry.get()
    setup_master_key(master_password)
    master_password_entry.delete(0, 'end')
    master_password_prompt.withdraw()

def main():
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
    
    add_entry_button = ttk.Button(root, text="Add an Entry", width=20)
    add_entry_button.pack(pady=10)

    retrieve_password_button = ttk.Button(root, text="Retrieve a Password", width=20)
    retrieve_password_button.pack(pady=10)

    quit_button = ttk.Button(root, text="Quit", width=20)
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

    submit_button = ttk.Button(master_password_prompt, text="Submit", command=lambda: on_submit_function(master_password_entry, root))
    submit_button.pack(pady=10)

    master_password_prompt.protocol("WM_DELETE_WINDOW", root.destroy)  # Close the app if the master password prompt is closed

    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()