#!/usr/bin/env python3

import hwmap
from sys import argv
import json

def main():
    if len(argv) != 3:
        print("Usage: %s eeprom-dump-file json-out-file" % argv[0])
        return
    
    with open(argv[1], "rb") as eeprom_file:
        eeprom = eeprom_file.read();

    mapping = {}
    for key_addr in hwmap.key_addrs:
        keycode = eeprom[key_addr]
        label = hwmap.find_key_label(keycode)
        if label is None:
            print("Could not find label for keycode:", hex(keycode),
                  "at:", hex(key_addr))
        mapping[hex(key_addr)] = label

    with open(argv[2], "w") as json_file:
        json_file.write(json.dumps(mapping, indent = 4))

if __name__ == "__main__":
    main()
