from setuptools import setup, find_packages

setup(
    name="passwordmanager",
    version="0.1",
    packages=find_packages(),
    install_requires=[
    "setuptools",
    "cffi",
    "argon2-cffi",
    "pyperclip",
    "cryptography",
    "pyinstaller"
    ],
    entry_points={
        "console_scripts": [
            "passwordmanager = cli_main:main",
        ],
    },
)