# A utility for modifying Kinesis Advantage key mappings

## Disclaimer
The programs here operate on an EEPROM dump from the keyboard.
This means that in order to use these the keyboard must be first
disassembled and the EEPROM chip removed, dumped and reprogrammed. This
will probably void your warranty and can damage the keyboard if done
incorrectly. Also an I2C EEPROM programmer is required. I take no
responsibility for any of the results of these programs and instructions.

## How are the key mappings stored?
The key mappings are stored on a 2KB I2C Flash chip on the main board of
the keyboard. The key mappings are stored as an array where each button
on the keyboard corresponds to an array index which contains the key to
which which the button has been mapped to.

I reverse engineered the mapping codes by swapping keys and around,
dumping the Flash chip and looking for patterns.

## How are the mapping modified
A set of programs are provided to convert the binary blob from the
keyboard into human modifiable json format and back to binary. Also
a program for creating an svg image visualizing the mappings is
provided.

# How to use this thing
## Removing the Flash chip
Disassemble the keyboard (and remember to unplug it first). Locate
the Flash chip labeled U2 on the keyboard main board. The chip should
be an 8-pin DIP chip in a socket. Carefully remove the chip the socket.

## Dump the flash chip
Place the chip in the EEPROM programmer.

I used a Minipro TL866CS programmer to read the chip:
```
% minipro -p "AT24C16B" -r original.bin
```
This step will be different depending on the programmer.

## Parse the dump into json
```
% ./eeprom-parse.py original.bin my-mappings.json
```

## Visualize the mappings
```
% ./json-to-svg my-mappings.json my-mappings.svg
```
The svg file contains a visualization of the mappings in `my-mappings.json`.
The dark orange coloured number is an identifier for the physical key and the
black text signifies the symbol currently assigned to it.

## Modifying the mappings
The json file contains entries like this:
```
    "0x26": "F4",
    "0x29": "LCtrl",
    "0x25": "F1",
```

There the hex number in quotes corresponds to the physical button identifier,
which is marked with dark orange in the visualization. You most likely don't
want to touch these. On the right side is the symbol to which that button is
assigned to these can be modified. A complete list of supported symbols can
be found in the `label_codes` array in `hwmap.py`. After modifying the
mappings it's a good idea to check the results by running the svg generator
from the previous step.

## Patching the EEPROM image
Run the patcher to create a modified EEPROM image.
```
% cp original.bin my-mappings.bin
% ./eeprom-patch.py my-mappings.json my-mappings.bin
```

## Flash the EEPROM
```
% minipro -p "AT24C16B" -w my-mappings.bin
```
This step will be different depending on the programmer.

## Cleanup
Place the EEPROM back into the socket in the keyboard and reassemble it.
The mappings should now be in effect.

# TODO
Mapping rest of the embedded layer (Keypad mode) keys.
Mapping foot pedals.

