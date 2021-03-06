""" Map EEPROM lookup table addresses into approximate physical key layout """
key_addrs = {
    0x15: { "x": 0, "y": 0, "w": 0.8 },
    0x25: { "x": 1, "y": 0, "w": 0.8 },
    0x1d: { "x": 2, "y": 0, "w": 0.8 },
    0x16: { "x": 3, "y": 0, "w": 0.8 },
    0x26: { "x": 4, "y": 0, "w": 0.8 },
    0x1e: { "x": 5, "y": 0, "w": 0.8 },
    0x17: { "x": 6, "y": 0, "w": 0.8 },
    0x27: { "x": 7, "y": 0, "w": 0.8 },
    0x1f: { "x": 8, "y": 0, "w": 0.8 },
    0x14: { "x": 9, "y": 0, "w": 0.8 },

    0x24: { "x": 10, "y": 0, "w": 0.8 },
    0x1c: { "x": 11, "y": 0, "w": 0.8 },
    0x13: { "x": 12, "y": 0, "w": 0.8 },
    0x23: { "x": 13, "y": 0, "w": 0.8 },
    0x1b: { "x": 14, "y": 0, "w": 0.8 },
    0x12: { "x": 15, "y": 0, "w": 0.8 },

    0x57: { "x": 0, "y": 1 },
    0x56: { "x": 0, "y": 2 },
    0x55: { "x": 0, "y": 3 },
    0x54: { "x": 0, "y": 4 },

    0x4f: { "x": 1, "y": 1 },
    0x4e: { "x": 1, "y": 2 },
    0x4d: { "x": 1, "y": 3 },
    0x4c: { "x": 1, "y": 4 },
    0x4b: { "x": 1, "y": 5 },

    0x47: { "x": 2, "y": 1 },
    0x46: { "x": 2, "y": 2 },
    0x45: { "x": 2, "y": 3 },
    0x44: { "x": 2, "y": 4 },
    0x43: { "x": 2, "y": 5 },

    0x3f: { "x": 3, "y": 1 },
    0x3e: { "x": 3, "y": 2 },
    0x3d: { "x": 3, "y": 3 },
    0x3c: { "x": 3, "y": 4 },
    0x3b: { "x": 3, "y": 5 },

    0x37: { "x": 4, "y": 1 },
    0x36: { "x": 4, "y": 2 },
    0x35: { "x": 4, "y": 3 },
    0x34: { "x": 4, "y": 4 },
    0x33: { "x": 4, "y": 5 },

    0x2f: { "x": 5, "y": 1 },
    0x2e: { "x": 5, "y": 2 },
    0x2d: { "x": 5, "y": 3 },
    0x2c: { "x": 5, "y": 4 },


    0x39: { "x": 4, "y": 7, "h": 2 },
    0x29: { "x": 5, "y": 6 },
    0x31: { "x": 5, "y": 7, "h": 2 },
    0x2a: { "x": 6, "y": 6 },
    0x3a: { "x": 6, "y": 7 },
    0x4a: { "x": 6, "y": 8 },


    0x51: { "x": 11, "y": 7, "h": 2 },
    0x41: { "x": 10, "y": 6 },
    0x49: { "x": 10, "y": 7, "h": 2 },
    0x30: { "x": 9, "y": 6 },
    0x40: { "x": 9, "y": 7 },
    0x50: { "x": 9, "y": 8 },


    0x5b: { "x": 10, "y": 1 },
    0x5a: { "x": 10, "y": 2 },
    0x59: { "x": 10, "y": 3 },
    0x58: { "x": 10, "y": 4 },

    0x63: { "x": 11, "y": 1 },
    0x62: { "x": 11, "y": 2 },
    0x61: { "x": 11, "y": 3 },
    0x60: { "x": 11, "y": 4 },
    0x5f: { "x": 11, "y": 5 },

    0x6b: { "x": 12, "y": 1 },
    0x6a: { "x": 12, "y": 2 },
    0x69: { "x": 12, "y": 3 },
    0x68: { "x": 12, "y": 4 },
    0x67: { "x": 12, "y": 5 },

    0x7b: { "x": 13, "y": 1 },
    0x72: { "x": 13, "y": 2 },
    0x79: { "x": 13, "y": 3 },
    0x78: { "x": 13, "y": 4 },
    0x77: { "x": 13, "y": 5 },

    0x83: { "x": 14, "y": 1 },
    0x82: { "x": 14, "y": 2 },
    0x81: { "x": 14, "y": 3 },
    0x80: { "x": 14, "y": 4 },
    0x7f: { "x": 14, "y": 5 },

    0x8b: { "x": 15, "y": 1 },
    0x8a: { "x": 15, "y": 2 },
    0x89: { "x": 15, "y": 3 },
    0x88: { "x": 15, "y": 4 },
}


beep_cfg_addr               = 0x06
beep_cfg_click_mask         = 0x01
beep_cfg_state_change_mask  = 0x2


""" Map between key labels and EEPROM lookup table entry codes """
label_codes = [
    ( "Esc",       0x05 ),
    ( "F1",        0x15 ),
    ( "F2",        0x0d ),
    ( "F3",        0x06 ),
    ( "F4",        0x16 ),
    ( "F5",        0x0e ),
    ( "F6",        0x07 ),
    ( "F7",        0x17 ),
    ( "F8",        0x0f ),
    ( "F9",        0x04 ),
 
    ( "F10",       0x14 ),
    ( "F11",       0x0c ),
    ( "F12",       0x03 ),
    ( "PrSc",      0x13 ),
    ( "ScLc",      0x0b ),
    ( "Pse",       0x02 ),

    ( "+",         0x47 ),
    ( "Tab",       0x46 ),
    ( "Caps",      0x45 ),
    ( "LShift",    0x44 ),

    ( "1",         0x3f ),
    ( "Q",         0x3e ),
    ( "A",         0x3d ),
    ( "Z",         0x3c ),
    ( "~",         0x3b ),

    ( "2",         0x37 ),
    ( "W",         0x36 ),
    ( "S",         0x35 ),
    ( "X",         0x34 ),
    ( "|",         0x33 ),

    ( "3",         0x2f ),
    ( "E",         0x2e ),
    ( "D",         0x2d ),
    ( "C",         0x2c ),
    ( "Left",      0x2b ),

    ( "4",         0x27 ),
    ( "R",         0x26 ),
    ( "F",         0x25 ),
    ( "V",         0x24 ),
    ( "Right",     0x23 ),

    ( "5",         0x1f ),
    ( "T",         0x1e ),
    ( "G",         0x1d ),
    ( "B",         0x1c ),


    ( "Bcksp",     0x29 ),
    ( "LCtrl",     0x19 ),
    ( "Delete",    0x21 ),
    ( "LAlt",      0x1a ),
    ( "Home",      0x2a ),
    ( "End",       0x3a ),


    ( "Spce",      0x41 ),
    ( "RCtrl",     0x31 ),
    ( "Enter",     0x39 ),
    ( "MdSw",      0x20 ),
    ( "PgUp",      0x30 ),
    ( "PgDn",      0x40 ),


    ( "6",         0x4b ),
    ( "Y",         0x4a ),
    ( "H",         0x49 ),
    ( "N",         0x48 ),

    ( "7",         0x53 ),
    ( "U",         0x52 ),
    ( "J",         0x51 ),
    ( "M",         0x50 ),
    ( "Up",        0x4f ),

    ( "8",         0x5b ),
    ( "I",         0x5a ),
    ( "K",         0x59 ),
    ( "<",         0x58 ),
    ( "Down",      0x57 ),

    ( "9",         0x6b ),
    ( "O",         0x62 ),
    ( "L",         0x69 ),
    ( ">",         0x68 ),
    ( "{",         0x67 ),

    ( "0",         0x73 ),
    ( "P",         0x72 ),
    ( ":",         0x71 ),
    ( "?",         0x70 ),
    ( "}",         0x6f ),

    ( "-",         0x7b ),
    ( "\\",        0x7a ),
    ( "\"",        0x79 ),
    ( "RShift",    0x78 ),

    ( "Insert",    0x01 ),
    ( "Menu",      0x28 ),
    ( "RSuper",    0x18 ),
    ( "LSuper",    0x22 ),
]

def find_key_label(keycode):
    for (label, code) in label_codes:
        if code == keycode:
            return label
    return None

def find_key_code(keylabel):
    for (label, code) in label_codes:
        if label == keylabel:
            return code
    return None
