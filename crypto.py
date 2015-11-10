#!/usr/bin/env python
import argparse
import lib.b64

def main():
    parser = argparse.ArgumentParser(description='Crypto some files.')
    parser.add_argument('--b64en', help = 'encode file with base64', nargs = 2, metavar = 'FILENAME')
    parser.add_argument('--b64de', help = 'decode file with base64', nargs = 2, metavar = 'FILENAME')

    args = parser.parse_args()
    if args.b64en:
        lib.b64.encode(args.b64en[0], args.b64en[1])
    elif args.b64de:
        lib.b64.decode(args.b64de[0], args.b64de[1])

if __name__ == '__main__':
    main()
