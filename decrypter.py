import os
import sys
import argparse
from cryptography.fernet import Fernet

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

def main():
    parser = argparse.ArgumentParser(description="Ransomware - Decrypter")
    parser.add_argument("--path", type=str, required=True, help="Path to directory or file")
    parser.add_argument("--key", type=str, required=True, help="Decryption key")

    key = parser.parse_args().key.encode()
    for root, dirs, files in os.walk(args.path):
        for file in files:
            decrypt_file(os.path.join(root, file), key)
    print("Decryption completed.")

if __name__ == "__main__":
    main()
