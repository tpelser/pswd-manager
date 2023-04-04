from database.db import db_config, add_password_data, get_password_data_by_website
from utils.clipboard import copy_to_clipboard
from utils.pwd_generator import generate_password, prompt_password_generation_options
from utils.master_key import setup_master_key, verify_master_password
from utils.encryption import decrypt_password, encrypt_password

def main():
    # run initial setup
    salt = setup_master_key()
    verified_master_password = None

    while True:
        master_password = input("Enter your master password: ")
        if verify_master_password(master_password):
            verified_master_password = master_password
            break
        else:
            print("Incorrect master password. Please try again.")
    # set up the database
    db_config()

    while True:
        # Ask the user for their choice
        choice = input("Enter 'A' to add an entry, 'R' to retrieve a password, or 'Q' to quit: ").upper()

        ###### Add an entry ######
        if choice=="A":
            # add an entry
            website = input("Enter the website URL: ")
            email = input("Enter the email: ")
            username = input("Enter the username (optional, press Enter to skip): ")
            password = input("Enter the password (press Enter to generate a random password): ")

            if not password:
                length, allow_numbers, allow_special_chars = prompt_password_generation_options()
                password = generate_password(length=length, allow_numbers=allow_numbers, allow_special_chars=allow_special_chars)
                print(f"Generated password: {password}")

            encrpyted_password = encrypt_password(password, verified_master_password, salt)
            add_password_data(website, email, username, encrpyted_password)
            print("Password data saved")

        #### Retrieve an entry ####
        elif choice == "R":
            website = input("Enter the website URL: ")
            password_data = get_password_data_by_website(website)

            if password_data:
                if password_data.username:
                    decrypted_password = decrypt_password(password_data.password_hash, verified_master_password, salt)
                    copy_to_clipboard(password_data.username)
                    print(f"Username: {password_data.username} \n Username copied to clipboard. Press Enter to copy the password.")
                    input()
                copy_to_clipboard(decrypted_password)
                print(f"PWD: {decrypted_password}. Password copied to clipboard.")
            else:
                print("No password data found for the given website.")

        elif choice == "Q":
            # Quit the program
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()