#!/usr/bin/env python3

# cli tool where you describe a pattern and it will search for it in the GPT-3 model
# usage: grept [the pattern you want to grep]
# example: 
# $ grept "include anything that starts with a capital J and ends with a lowercase e"
# $ grep '^J.*e$'
# $ echo -e "Jme\nand Jam" | grep '^J.*e$'
# Jme

import sys
import re
import argparse

def query_gpt(described_pattern):
    # query GPT-3.5 Turbo with the described pattern
    pass

def validate_pattern(recommended_pattern):
    # validate the recommended pattern
    pass

def main():
    parser = argparse.ArgumentParser(description='Grep for patterns in GPT-3.5 Turbo')
    parser.add_argument('-x', '--explain', action='store_true', help='Break down what the pattern is doing')
    parser.add_argument('-y', '--yolo', action='store_true', help='grep first, ask questions later')
    args = parser.parse_args()
    
    described_pattern = ' '.join(sys.argv[1:])
