from database.db import db_config, add_password_data, get_password_data_by_website
from utils.hashing import verify_password
from utils.clipboard import copy_to_clipboard
from utils.pwd_generator import generate_password
from utils.master_key import setup_master_key, verify_master_password

def main():
    # set up the database
    db_config()
    # set up the master key
    device_secret = setup_master_key()

    while True:
        master_password = input("Enter your master password: ")
        if verify_master_password(master_password):
            break
        else:
            print("Incorrect master password. Please try again.")
    
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
                length = input("Enter the desired password length (press enter for Default 12 characters): ")
                include_numbers = input("Allow numbers? Press Enter for Yes or type 'no' to disallow: ").upper()
                include_special_chars = input("Allow special characters (e.g. !+*#, etc.)? Press Enter for Yes, or type 'no' to disallow: ").upper()
                if not length:
                    length = 12
                else:
                    length = int(length)

                if include_numbers=="YES":
                    include_numbers==True

                if include_special_chars=="Yes"
                    include_special_chars==True
                else:
                    include_special_chars==False

                password = generate_password(length=length, include_numbers=include_numbers, include_special_chars=include_special_chars)
                print(f"Generated password: {password}")

            add_password_data(website, email, username, password)
            print("Password data saved")

        #### Retrieve an entry ####
        elif choice == "R":
            website = input("Enter the website URL: ")
            password_data = get_password_data_by_website(website)

            if password_data:
                if password_data.username:
                    copy_to_clipboard(password_data.username)
                    print("Username copied to clipboard. Press Enter to copy the password.")
                    input()
                copy_to_clipboard(password_data.password)
                print("Password copied to clipboard.")
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