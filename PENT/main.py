import os
import base64
from time import sleep
from cryptography.fernet import Fernet
from pyfiglet import figlet_format
from colorama import init, Fore

init()

def print_banner():
    banner = figlet_format("pent", font="cybermedium").capitalize()
    print(Fore.RED + banner)
    print(Fore.GREEN + "Welcome to PENT Python Text and File Encryption Tool ---- Discord: UNDEAD#0155")
    print(Fore.GREEN + "Version 1.0")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def generate_key(password):
    key = Fernet.generate_key()
    encoded_key = base64.urlsafe_b64encode(key)
    with open(f"{password}.key", "wb") as key_file:
        key_file.write(encoded_key)

def load_key(password):
    with open(f"{password}.key", "rb") as key_file:
        encoded_key = key_file.read()
        key = base64.urlsafe_b64decode(encoded_key)
        return key

def encrypt_text(text, password):
    key = load_key(password)
    f = Fernet(key)
    encrypted_text = f.encrypt(text.encode())
    return encrypted_text

def decrypt_text(encrypted_text, password):
    key = load_key(password)
    f = Fernet(key)
    decrypted_text = f.decrypt(encrypted_text).decode()
    return decrypted_text

def encrypt_file(file_path, password):
    key = load_key(password)
    f = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(f"{file_path}.encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_file(file_path, password):
    key = load_key(password)
    f = Fernet(key)
    with open(file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(f"{os.path.splitext(file_path)[0]}.decrypted{os.path.splitext(file_path)[1]}", "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

def main():
    clear_screen()
    print_banner()
    sleep(3)
    clear_screen()

    option = input(Fore.YELLOW + "01. Encrypt file\n02. Encrypt text\n03. Decrypt file\n04. Decrypt text\n00. Exit\n Enter your option: ")

    if option in ["1", "01"]:
        file_path = input("Enter the path of the file to encrypt: ")
        password = input("Enter a password: ")
        generate_key(password)
        encrypt_file(file_path, password)
        print("Path to encrypted file:"+ file_path)

    elif option in ["2", "02"]:
        text = input("Enter some text to encrypt: ")
        password = input("Enter a password: ")
        generate_key(password)
        encrypted_text = encrypt_text(text, password)
        print(f"Encrypted text: {encrypted_text}")

    elif option in ["3", "03"]:
        file_path = input("Enter the path of the encrypted file to decrypt: ")
        password = input("Enter the password: ")
        decrypt_file(file_path, password)

    elif option in ["4", "04"]:
        encrypted_text = input("Enter the encrypted text: ")
        password = input("Enter the password: ")
        decrypted_text = decrypt_text(encrypted_text, password)
        print(f"Decrypted text: {decrypted_text}")

    elif option in ["0", "00", "exit"]:
        print(Fore.RED + "Exiting...")
        sleep(2)
        print("Thanks for using PENT! :)")

    else:
        print(Fore.RED + "Invalid option")
        sleep(2)
        print("Thanks for using PENT! :)")

if __name__ == "__main__":
    main()