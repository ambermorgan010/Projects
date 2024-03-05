"""
PURPOSE: Decodes common messaging/chat acronyms.

Supports the following acronyms:
 * AKA - also known as
 * BRB - be right back
 * BTW - by the way
 * FYI - for your information
 * IRL - in real life
 * LOL - laughing out loud
 * TTYL - talk to you later
 * YOLO - you only live once

AUTHOR: Amber Morgan
"""

def main():
    meanings = {"AKA": "also known as", "BRB": "be right back", "BTW": "by the way", "FYI": "for your information", "IRL": "in real life", "LOL": "laughing out loud", "TTYL": "talk to you later", "YOLO": "you only live once"}
    acronym = input("Enter an acronym: ")
    definition = meanings[acronym]
    print("{a} means {d}.".format(a=acronym, d=definition))


if __name__ == "__main__":
    main()
