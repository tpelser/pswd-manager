from argon2 import PasswordHasher

# Initialise the Argon2 password hasher
ph = PasswordHasher()

def hash_password(password: str) -> str:
    """
    Hash a given password using the Argon2 password hashing algorithm
    """
    password_hash = ph.hash(password)
    return password_hash

def verify_password(password: str, password_hash: str) -> bool:
    """
    Verify whether the given password matches the provided Argon2 password hash
    """
    try:
        ph.verify(password_hash, password)
        return True
    except:
        return False