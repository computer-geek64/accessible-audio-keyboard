#!/usr/bin/python3
# Main.py
# Ashish D'Souza
# November 15th, 2018

import os
import numpy as np
from Keyboard import Layout


def print_keyboard(keyboard_layout, selection):
    if len(np.shape(selection)) == 0:
        for row in range(len(keyboard_layout)):
            if row != selection:
                print(" ".join(keyboard_layout[row]))
            else:
                print("[ " + " ".join(keyboard_layout[row]) + " ]")
    else:
        for row in range(len(keyboard_layout)):
            line = ""
            for col in range(len(keyboard_layout[row])):
                if [row, col] != selection:
                    line += keyboard_layout[row][col] + " "
                else:
                    line += "[ " + keyboard_layout[row][col] + " ] "
            print(line[:-1])


keyboard = Layout()

text = ""
row = 0
while True:
    print_keyboard(keyboard.keyboard, row)
    if input(text + "\n") == " ":
        col = 0
        print_keyboard(keyboard.keyboard, [row, col])
        while input(text + "\n") != " ":
            col += 1
            if col >= len(keyboard.keyboard[row]):
                col = 0
            print_keyboard(keyboard.keyboard, [row, col])
        text += keyboard.keyboard[row][col]
        keyboard.set_words(keyboard.get_words(text, shift=False))
        keyboard.set_alphabet(keyboard.get_alphabet(text, shift=False))
        row = -1
    row += 1
    if row >= len(keyboard.keyboard):
        row = 0
