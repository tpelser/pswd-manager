import secrets
import string

def prompt_password_generation_options():
    # prompt for pswd length
    length = input("Enter the desired password length (press Enter for 12 characters) ")
    length = int(length) if length else 12

    #prompt for allowing numbers
    allow_numbers = input("Allow numbers? Press Enter for yes, or type 'no' to disallow: ").lower()
    allow_numbers = allow_numbers != "no"

    #prompt for allowing special characters
    allow_special_chars = input("Allow special characters? Press Enter for yes, or type 'no' to disallow: ").lower()

def generate_password(length=12, include_numbers=True, include_special_chars=True):
    # Define the character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    numbers = string.digits if include_numbers else ""
    special_chars = string.punctuation if include_special_chars else ""

    # combine the character sets
    password_characters = lowercase_chars + uppercase_chars + numbers + special_chars

    # Generate a random password
    pwd = ''.join(secrets.choice(password_characters) for i in range(length))

    return pwd