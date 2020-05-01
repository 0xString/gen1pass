"""
███████╗██████╗ ██████╗ ██╗███╗   ██╗ ██████╗ 
██╔════╝██╔══██╗██╔══██╗██║████╗  ██║██╔════╝ 
███████╗██████╔╝██████╔╝██║██╔██╗ ██║██║  ███╗
╚════██║██╔═══╝ ██╔══██╗██║██║╚██╗██║██║   ██║
███████║██║     ██║  ██║██║██║ ╚████║╚██████╔╝
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝
-- gen1pass.py written by spring --
-- https://github.com/Zpring/gen1pass --
"""

import random
import string
import argparse
import pyperclip


def randomStringLower(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def randomStringUpper(stringLength=8):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def randomStringLowUpper(stringLength=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))


def randomStringNumber(stringLength=8):
    numbers = string.digits
    return ''.join(random.choice(numbers) for i in range(stringLength))


def randomStringLowNumber(stringLength=8):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))


def randomStringUpNumber(stringLength=8):
    letters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))


def randomStringLowUpNumber(stringLength=8):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))


def randomStringSymbol(stringLength=8):
    symbols = string.punctuation
    return ''.join(random.choice(symbols) for i in range(stringLength))


def randomStringLowSym(stringLength=8):
    letters = string.ascii_lowercase + string.punctuation
    return ''.join(random.choice(letters) for i in range(stringLength))


def randomStringUpSym(stringLength=8):
    letters = string.ascii_uppercase + string.punctuation
    return ''.join(random.choice(letters) for i in range(stringLength))


def randomStringLowUpSym(stringLength=8):
    letters = string.ascii_letters + string.punctuation
    return ''.join(random.choice(letters) for i in range(stringLength))


def randomStringLowUpSymNum(stringLength=8):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(stringLength ))


parser = argparse.ArgumentParser()

parser.add_argument('-l', '--lower', action='store_true', 
    help="generate lowercase ")

parser.add_argument('-u', '--upper', action='store_true', 
    help="generate uppercase ")

parser.add_argument('-lu', '--lowerupper', action='store_true', 
    help="generate lowercase, uppercase ")

parser.add_argument('-n', '--number', action='store_true', 
    help="generate number ")

parser.add_argument('-un', '--uppernumber', action='store_true', 
    help="generate uppercase, number ")

parser.add_argument('-ln', '--lowernumber', action='store_true', 
    help="generate lowercase, number ")

parser.add_argument('-lun', '--loweruppernumber', action='store_true', 
    help="generate lowercase, uppercase, number ")

parser.add_argument('-s', '--symbol', action='store_true', 
    help="generate symbol ")

parser.add_argument('-us', '--uppersymbol', action='store_true', 
    help="generate upper, symbol ")

parser.add_argument('-ls', '--lowersymbol', action='store_true', 
    help="generate lowercase, symbol ")

parser.add_argument('-lus', '--loweruppersymbol', action='store_true', 
    help="generate lowercase, uppercase, symbol ")

parser.add_argument('-lusn', '--loweruppersymbolnumber', action='store_true', 
    help="generate lowercase, uppercase, symbol, number ")


parser.add_argument('length', type=int, help="length of the password")

args = parser.parse_args()

if args.lower:
    if args.length < 0:
        args.length = 8

    passwd = randomStringLower(args.length)
    pyperclip.copy(passwd)
    print(f'{passwd}\nText copied to clipboard.')

elif args.upper:
    if args.length < 0:
        args.length = 8

    passwd = randomStringUpper(args.length)
    pyperclip.copy(passwd)
    print(f'{passwd}\nText copied to clipboard.')

elif args.lowerupper:
    if args.length < 0:
        args.length = 8

    passwd = randomStringLowUpper(args.length)
    pyperclip.copy(passwd)
    print(f'{passwd}\nText copied to clipboard.')

elif args.number:
    if args.length < 0:
        args.length = 8

    passwd = randomStringNumber(args.length)
    pyperclip.copy(passwd)
    print(f'{passwd}\nText copied to clipboard.')

elif args.lowernumber:
    if args.length < 0:
        args.length = 8

    passwd = randomStringLowNumber(args.length)
    pyperclip.copy(passwd)
    print(f'{passwd}\nText copied to clipboard.')

elif args.uppernumber:
    if args.length < 0:
        args.length = 8

    passwd = randomStringUpNumber(args.length)
    pyperclip.copy(passwd)
    print(f'{passwd}\nText copied to clipboard.')

elif args.loweruppernumber:
    if args.length < 0:
        args.length = 8

    passwd = randomStringLowUpNumber(args.length)
    pyperclip.copy(passwd)
    print(f'{passwd}\nText copied to clipboard.')

elif args.symbol:
    if args.length < 0:
        args.length = 8

    passwd = randomStringSymbol(args.length)
    pyperclip.copy(passwd)
    print(f'{passwd}\nText copied to clipboard.')

elif args.lowersymbol:
    if args.length < 0:
        args.length = 8

    passwd = randomStringLowSym(args.length)
    pyperclip.copy(passwd)
    print(f'{passwd}\nText copied to clipboard.')

elif args.uppersymbol:
    if args.length < 0:
        args.length = 8

    passwd = randomStringUpSym(args.length)
    pyperclip.copy(passwd)
    print(f'{passwd}\nText copied to clipboard.')

elif args.loweruppersymbol:
    if args.length < 0:
        args.length = 8

    passwd = randomStringLowUpSym(args.length)
    pyperclip.copy(passwd)
    print(f'{passwd}\nText copied to clipboard.')

elif args.loweruppersymbolnumber:
    if args.length < 0:
        args.length = 8

    passwd = randomStringLowUpSymNum(args.length)
    pyperclip.copy(passwd)

    print(f'{passwd}\nText copied to clipboard.')

else:
    passwd = randomStringLower(args.length)
    pyperclip.copy(passwd)

    print(f'{passwd}\nText copied to clipboard.')

