import math

def shift_letter(letter, shift):
    if len(letter) != 1 or not (letter.isalpha() or letter == " "):
        raise ValueError("Input must be a single letter or a space, not a word.")
    letter = letter.upper()
    if letter == " ":
        return " "
    new_position = (ord(letter) - ord("A") + shift) % 26
    return chr(ord("A") + new_position)

def caesar_cipher(message, shift):
    return "".join(shift_letter(letter, shift) for letter in message)

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    shift = ord(letter_shift.upper()) - ord("A")
    return shift_letter(letter, shift)

def vigenere_cipher(message, key):
    extended_key = (key * (len(message) // len(key))) + key[:len(message) % len(key)]
    
    print(f"Message: {message}")
    print(f"Extended Key: {extended_key}")
    
    encrypted_message = ""
    
    for m, k in zip(message, extended_key):
        if m != " ":
            print(f"Shifting letter: {m} by {k}")
        encrypted_message += shift_by_letter(m, k) if m != " " else " "
    
    return encrypted_message

def scytale_cipher(message, shift):
    while len(message) % shift != 0:
        message += "_"
    num_columns = len(message) // shift
    return "".join(
        message[(i // shift) + num_columns * (i % shift)] for i in range(len(message))
    )

def scytale_decipher(message, shift):
    num_columns = len(message) // shift
    return "".join(
        message[(i // num_columns) + shift * (i % num_columns)] for i in range(len(message))
    )
