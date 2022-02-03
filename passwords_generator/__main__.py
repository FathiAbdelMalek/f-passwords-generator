import random
import sys
import pyperclip
from passwords_generator.generator import PassGen


def main():
    k = ''
    if len(sys.argv) >= 3:
        t = sys.argv[1]
        k = sys.argv[2]
    elif len(sys.argv) >= 2:
        t = sys.argv[1]
    else:
        t = input("Enter the text   : ")
    if k == '':
        for _ in range(random.randint(4, 6)):
            k += (chr(random.randint(97, 122)))
    password = PassGen(t, k)
    password.generate_password()
    p = password.code
    print("The Text Is                      : {}".format(t))
    print("The Key Is                       : {}".format(k))
    print("The Ciphered Text Is             : {}".format(p))
    try:
        pyperclip.copy(p)
        print("The Password has been copied to your clipboard, just past it")
    except:
        print("Your system hasn't copy/paste mechanism, if you on linux try to install one, eg: xclip")


if __name__ == '__main__':
    main()
