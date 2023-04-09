import tkinter as tk
from tkinter import ttk

# prompt for password generation options
def prompt_password_generation_options(root):
    def on_submit_options():
        nonlocal length, allow_numbers, allow_special_chars
        length = int(length_entry.get())
        allow_numbers = allow_numbers_var.get()
        allow_special_chars = allow_special_chars_var.get()
        options_window.destroy()

    options_window = tk.Toplevel(root)
    options_window.title("Password Generation Options")
    options_window.geometry("400x200")

    length = 12
    allow_numbers = True
    allow_special_chars = True

    ttk.Label(options_window, text="Password length:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    length_entry = ttk.Entry(options_window)
    length_entry.insert(0, "12")  # Insert default value
    length_entry.grid(row=0, column=1, padx=10, pady=10)

    allow_numbers_var = tk.BooleanVar()
    allow_numbers_var.set(True)  # Set default value
    allow_numbers_checkbutton = ttk.Checkbutton(options_window, text="Allow numbers", variable=allow_numbers_var)
    allow_numbers_checkbutton.grid(row=1, column=0, padx=10, pady=10, sticky='w')

    allow_special_chars_var = tk.BooleanVar()
    allow_special_chars_var.set(True)  # Set default value
    allow_special_chars_checkbutton = ttk.Checkbutton(options_window, text="Allow special characters", variable=allow_special_chars_var)
    allow_special_chars_checkbutton.grid(row=1, column=1, padx=10, pady=10, sticky='w')

    submit_button = ttk.Button(options_window, text="Submit", command=on_submit_options)
    submit_button.grid(row=2, column=1, padx=10, pady=10)

    options_window.grab_set()  # Make the options window modal
    root.wait_window(options_window)  # Wait for the window to close

    return length, allow_numbers, allow_special_chars