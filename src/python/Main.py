#!/usr/bin/python3
# Main.py
# Ashish D'Souza
# November 15th, 2018

import os
import numpy as np
from Keyboard import Layout
from gtts import gTTS


def speak(text):
    gTTS(text, lang="en").save("speak.mp3")
    os.system("mpg123 speak.mp3; rm speak.mp3")


def print_keyboard(keyboard_layout, selection):
    if len(np.shape(selection)) == 0:
        for row in range(len(keyboard_layout)):
            if row != selection:
                print(" ".join(keyboard_layout[row]))
            else:
                print("[ " + " ".join(keyboard_layout[row]) + " ]")
                for col in range(len(keyboard_layout[row])):
                    speak(keyboard_layout[row][col])
    else:
        for row in range(len(keyboard_layout)):
            line = ""
            for col in range(len(keyboard_layout[row])):
                if [row, col] != selection:
                    line += keyboard_layout[row][col] + " "
                else:
                    line += "[ " + keyboard_layout[row][col] + " ] "
                    speak(keyboard_layout[row][col])
            print(line[:-1])


def get_text(keyboard, text, selection):
    if keyboard.keyboard[selection[0]][selection[1]] == "Backspace":
        return text[:-1]
    elif keyboard.keyboard[selection[0]][selection[1]] == "Clear":
        return ""
    elif keyboard.keyboard[selection[0]][selection[1]] == "Speak":
        gTTS(text, lang="en").save("speak.mp3")
        os.system("mpg123 speak.mp3; rm speak.mp3")
        return
    elif keyboard.keyboard[selection[0]][selection[1]] == "Shift":
        return
    elif keyboard.keyboard[selection[0]][selection[1]] == "0-9":
        return
    elif keyboard.keyboard[selection[0]][selection[1]] == "Del_Word":
        if len(text.split(" ")) == 1:
            return ""
        else:
            return " ".join(text.split(" ")[:-1]) + " "
    elif keyboard.keyboard[selection[0]][selection[1]] == "Settings":
        return
    else:
        return text + keyboard.keyboard[selection[0]][selection[1]]


keyboard = Layout()


text = ""
row = 0
while True:
    print("Text: " + text)
    print_keyboard(keyboard.keyboard, row)
    if input(">> ") != "":
        for col in range(len(keyboard.keyboard[row])):
            print_keyboard(keyboard.keyboard, [row, col])
            if input(">> ") != "":
                text = get_text(keyboard, text, [row, col])
                keyboard.set_words(keyboard.get_words(text, shift=False))
                keyboard.set_alphabet(keyboard.get_alphabet(text, shift=False))
                row = 0
                break
        row -= 1
    row += 1
    if row == len(keyboard.keyboard):
        row = 0
