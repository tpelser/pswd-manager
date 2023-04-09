# Password manager

This Password Manager is a powerful and user-friendly desktop application built using Python, Tkinter, the Fernet symmetric encryption standard, and SQLite database. It securely stores your passwords, making it easier to manage and retrieve them when needed. The intuitive graphical user interface makes using the application a breeze, even for users with no technical background.

## Features

* Securely store your passwords using strong encryption
* Create and store master passwords to secure your password database
* Generate strong, random passwords for your accounts
* Copy passwords to your clipboard for easy access
* Easily add, retrieve, and manage your passwords
* User-friendly interface with intuitive controls

## Built With

* **Python**: A versatile and powerful programming language used to build the core functionality of the Password Manager.
* **Tkinter**: A standard Python library that provides a fast and easy way to create a graphical user interface for the application.
* **Fernet encryption**: A symmetric encryption method that ensures your passwords are securely stored and can only be decrypted using your unique master password.
* **SQLite**: A lightweight, serverless, and self-contained SQL database engine used to store your password data securely.

## Security 

This Password Manager encrypts your passwords using the Fernet symmetric encryption standard, which ensures that your passwords can only be accessed using your unique master password and a random device secret. 

However, please be aware that no system is perfect, and there are potential risks involved with storing your sensitive information in any application. It is essential to follow best security practices, such as using strong, unique passwords and keeping your master password secure. Additionally, make sure to keep your operating system and software up to date to minimize vulnerabilities. 

Some security issues: 
1. The SQLite database itself is not yet encyrpted, only the passwords inside it are. 
2. The database is stored locally, rather than on a secure server.

This project is more of a fun learning project than a seriously secure application. **Use at your own risk.**

## Contribute
Feel free to fork this repository, make improvements, and submit pull requests. Your contributions are always welcome!

## License
This Password Manager is open-source software licensed under the MIT License.

## Disclaimer
The developer of this Password Manager is not responsible for any loss of data, compromised security, or any other issues that may arise from the use of this application. Please use it responsibly and at your own risk.