#!/usr/bin/env python3

import hwmap
from sys import argv
import json

def main():
    if len(argv) != 3:
        print("Usage: %s json-in-file eeprom-file" % argv[0])
        return

    with open(argv[1], "r") as json_file:
        mapping = json.load(json_file)

    with open(argv[2], "rb") as eeprom_file:
        eeprom = bytearray(eeprom_file.read())

    for addr, label in mapping.items():
        code = hwmap.find_key_code(label)
        if not code:
            print("Could not find keycode for label:", label)
        eeprom[int(addr, 16)] = code

    with open(argv[2], "wb") as eeprom_file:
        eeprom_file.write(eeprom)

if __name__ == "__main__":
    main()
