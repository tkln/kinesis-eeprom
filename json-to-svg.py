#!/usr/bin/env python3

import xml.etree.cElementTree as ET
import json
from sys import argv

import hwmap

def key_rect(root, x, y, label, addr, w = 1, h = 1):
    grid = 64
    key_sz = 0.9
    r = ET.SubElement(root, "rect", attrib = {
            "width": str(grid * key_sz * w),
            "height": str(grid * key_sz * h),
            "fill": "none",
            "stroke": "#000000",
            "stroke-width": "3",
            "rx": "10", "ry": "10",
            "x": str(x * grid),
            "y": str(y * grid)
        }
    )

    t = ET.SubElement(root, "text", attrib = {
            "x": str(x * grid + 6), "y": str(y * grid + 20)
        }
    ).text = label

    o = ET.SubElement(root, "text", attrib = {
            "x": str(x * grid + 6), "y": str(y * grid + 37),
            "fill": "chocolate",
        }
    ).text = addr

    return (r, t, o)

def main():
    if len(argv) != 3:
        print("Usage: %s json-in-file svg-out-file" % argv[0])
        return

    root = ET.Element("svg", attrib = {
            "version": "1.1", "xmlns": "http://www.w3.org/2000/svg",
            "xmlns:xlink": "http://www.w3.org/1999/xlink",
            "xml:space": "preserve"
            }
        )

    with open(argv[1], "r") as json_file:
        mapping = json.load(json_file)

    for addr, sym in mapping.items():
        pos = hwmap.key_addrs[int(addr, 16)];
        key_rect(root, pos["x"], pos["y"], sym, addr,
                 pos["w"] if "w" in pos else 1,
                 pos["h"] if "h" in pos else 1)
    tree = ET.ElementTree(root)
    tree.write(argv[2])

if __name__ == "__main__":
    main()
