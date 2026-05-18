# quick-pass

A tiny command‑line utility written in Python that generates a random password.

## Features
- Choose length (default 12)
- Include/exclude symbols, numbers, uppercase, lowercase
- One‑liner output, suitable for scripts

## Installation
```bash
# Clone the repository (or just copy the file)
git clone https://github.com/yourname/quick-pass.git
cd quick-pass
python3 -m venv .venv
source .venv/bin/activate
# No external dependencies needed; uses only the standard library
```

## Usage
```bash
python3 password_generator.py           # default 12‑char password
python3 password_generator.py 20        # 20‑character password
python3 password_generator.py -s -n    # symbols & numbers only
```

## Options
- `-l`, `--length` : length of the password (int)
- `-u`, `--no-uppercase` : exclude uppercase letters
- `-d`, `--no-lowercase` : exclude lowercase letters
- `-n`, `--no-digits` : exclude digits
- `-s`, `--no-symbols` : exclude symbols

## License
MIT License (see the LICENSE file in the full version).
