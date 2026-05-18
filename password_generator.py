#!/usr/bin/env python3
"""quick-pass: generate a random password.

Usage examples:
  python3 password_generator.py            # 12‑char password, all classes
  python3 password_generator.py 20         # custom length
  python3 password_generator.py -s -n     # symbols & numbers only
"""

import argparse
import secrets
import string
import sys

def build_charset(include_upper=True, include_lower=True, include_digits=True, include_symbols=True):
    charset = ''
    if include_upper:
        charset += string.ascii_uppercase
    if include_lower:
        charset += string.ascii_lowercase
    if include_digits:
        charset += string.digits
    if include_symbols:
        charset += string.punctuation
    if not charset:
        raise ValueError('At least one character class must be selected')
    return charset

def generate_password(length: int, charset: str) -> str:
    return ''.join(secrets.choice(charset) for _ in range(length))

def parse_args(argv=None):
    parser = argparse.ArgumentParser(description='Generate a secure random password')
    parser.add_argument('length', nargs='?', type=int, default=12,
                        help='Length of the password (default: 12)')
    parser.add_argument('-u', '--no-uppercase', action='store_true',
                        help='Exclude uppercase letters')
    parser.add_argument('-d', '--no-lowercase', action='store_true',
                        help='Exclude lowercase letters')
    parser.add_argument('-n', '--no-digits', action='store_true',
                        help='Exclude digits')
    parser.add_argument('-s', '--no-symbols', action='store_true',
                        help='Exclude symbols')
    return parser.parse_args(argv)

def main():
    args = parse_args()
    try:
        charset = build_charset(
            include_upper=not args.no_uppercase,
            include_lower=not args.no_lowercase,
            include_digits=not args.no_digits,
            include_symbols=not args.no_symbols,
        )
    except ValueError as e:
        sys.stderr.write(str(e) + '\n')
        sys.exit(1)
    password = generate_password(args.length, charset)
    print(password)

if __name__ == '__main__':
    main()
