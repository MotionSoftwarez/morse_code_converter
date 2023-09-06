"""
Author: Pawan Kumar Sharma
This script converts text in morse code
"""


def convert_morse_code(user_input):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': ' '
    }
    morse_code_to_numbers_dict = {
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }
    final_text = []
    for current_char in user_input:
        if current_char.isdigit():
            final_text.append(morse_code_to_numbers_dict[current_char.upper()])
        else:
            final_text.append(morse_code_dict[current_char.upper()])
    complete_code = " ".join(final_text)
    print(complete_code)


if __name__ == '__main__':
    user_input = input('Enter Your Text: ')
    convert_morse_code(user_input)
