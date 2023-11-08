import board
import digitalio
import time

# Dictionary representing the morse code chart
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ':'/'}

modifier = 0.25
dot_time = 1*modifier
dash_time = 3*modifier
between_taps = 1*modifier
between_letters = 3*modifier
between_words = 7*modifier

Bled = digitalio.DigitalInOut(board.GP0) # Sets the pin of the Blue LED
Bled.direction = digitalio.Direction.OUTPUT

while True:
    print("Enter Morse Code Message, or enter -q to quit:")
    Text = input() #Get the input from the user
    if Text == "-q": #If they type -q it quits 
        print("Quit")
        break #end the code
    else: 
        Up_Text = Text.upper() #Make all text uppercase
        for letter in Up_Text: #Go through each letter in the word
            print(MORSE_CODE[f"{letter}"], end=" ") #Print each letter in morse
        for letter in Up_Text: #Go through each letter in the word
            Flash = MORSE_CODE[letter]
            if Flash == ".":
                Bled.value = True
                time.sleep(dot_time)
            if Flash == "-":
                Bled.value = True
                time.sleep(dash_time)
            elif Flash == " ":
                Bled.value = False
                time.sleep(between_letters)
            elif Flash == "/":
                Bled.value = False
                time.sleep(between_words)
            Bled.value = False
            time.sleep(between_taps)
        