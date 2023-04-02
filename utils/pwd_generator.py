import secrets
import string

def generate_password(lenght=12, include_numbers=True, include_special_chars=True):
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