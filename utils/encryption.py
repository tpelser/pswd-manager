from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import base64

def create_fernet_key(master_password, salt):
    backend = default_backend()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
    )
    key = kdf.derive(master_password.encode())
    return Fernet(base64.urlsafe_b64encode(key))

def encrypt_password(password, master_password, salt):
    fernet = create_fernet_key(master_password, salt)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password, master_password, salt):
    fernet = create_fernet_key(master_password, salt)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password