#!/bin/python3
import random
import argparse
import pyperclip
from passwords_generator import PasswordGenerator


def get_key_phrase():
    key = input("Do you want to use a custom key? (y/N)").strip().lower()
    if key == 'y':
        return input("Enter the key: ")
    else:
        return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(4, 6)))


def generate_password(text, key, with_matrix):
    pass_gen = PasswordGenerator(text, key)
    pass_gen.generate_password()
    print(f"The Text is:              {text}")
    print(f"The Key is:               {key}")
    print(f"The Ciphered Text is:     {pass_gen.password}")
    if with_matrix:
        print(f"The Matrix used:")
        for row in pass_gen.matrix:
            print(" " * 25, row)

    try:
        pyperclip.copy(pass_gen.password)
        print("Your password has been copied to your clipboard. Just paste it")
    except pyperclip.PyperclipException:
        print("Your system doesn't have a copy/paste mechanism. If you are on Linux, try installing one (e.g., xclip)")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Strong Passwords Generator made with Python")
    parser.add_argument("-t", "--text", nargs='+', help="The plain text you want to encode")
    parser.add_argument("-k", "--key", help="The key phrase")
    parser.add_argument("-m", "--matrix", action="store_true", help="Show the used matrix in the encryption")
    args = parser.parse_args()

    plain_text = " ".join(args.text) if args.text else input("Enter the text: ")
    key_phrase = args.key if args.key else get_key_phrase()
    with_matrix = args.matrix

    generate_password(plain_text, key_phrase, with_matrix)
