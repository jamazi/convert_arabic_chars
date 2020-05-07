#!/usr/bin/env python3

import sys
import argparse


ar_chars_dict = {
    u'ذ': '`', u'ض': 'q', u'ص': 'w', u'ث': 'e', u'ق': 'r', u'ف': 't', u'غ': 'y', u'ع': 'u', u'ه': 'i', u'خ': 'o', u'ح': 'p', u'ج': '[', u'د': ']',
    u'ش': 'a', u'س': 's', u'ي': 'd', u'ب': 'f', u'ل': 'g', u'ا': 'h', u'ت': 'j', u'ن': 'k', u'م': 'l', u'ك': ';', u'ط': "'",
    u'ئ': 'z', u'ء': 'x', u'ؤ': 'c', u'ر': 'v', u'ﻻ': 'b', u'ى': 'n', u'ة': 'm', u'و': ',', u'ز': '.', u'ظ': '/',
    ' ': ' ', '\n': '', u'؟': '?',
    '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '0': '0',
    u'أ': 'H', u'إ': 'Y', u'آ': 'N',
}


def replace_chars(text: str):
    line = ""
    abnormal_chars = []
    for cch in text:
        try:
            line += ar_chars_dict[cch]
        except KeyError:
            line += cch
            if cch not in abnormal_chars:
                abnormal_chars.append(cch)
    if len(abnormal_chars) > 0:
        print(f"Abnormal chars: {', '.join(x.encode('unicode_escape').decode('utf8') for x in abnormal_chars)}", file=sys.stderr)
    return line


def main(arguments):
    parser = argparse.ArgumentParser(
        description="This python script will convert every arabic character in a wordlist to it's corresponding english character in QWERTY keyboard layout and print it in stdout.", formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input", help="input arabic wordlist", type=argparse.FileType('r'))
    args = parser.parse_args(arguments)
    for line in args.input.readlines():
        print(replace_chars(line))


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
