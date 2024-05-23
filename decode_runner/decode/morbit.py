numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bigram = ["..", ".-", "./", "-.", "--", "-/", "/.", "/-", "//"]
key_sorted = sorted("AZERTYUIO")
index_numeric = dict(zip(key_sorted, numbers))

key = "AZERTYUIO"
ordered_values = [index_numeric[letter] for letter in key]

# Associate each letter with its corresponding bigram
bigram_dict = dict(zip(ordered_values, bigram))

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '!': '-.-.--', '@': '.--.-.', ' ': ' '
}

def decode_morse(morse_code):
    morse_code = morse_code.split(' ')
    decoded_message = ''
    for code in morse_code:
        for key, value in MORSE_CODE_DICT.items():
            if code == value:
                decoded_message += key
    return decoded_message

def morbit_decoder(encoded_word):
    split_word = [encoded_word[i:i+1] for i in range(0, len(encoded_word), 1)]
    
    decoded_word = []
    # Check and replace number with the corresponding bigram
    for number in split_word:
        # Convertir number en entier avant la vérification
        num_int = int(number)
        if num_int in bigram_dict:
            decoded_word.append(bigram_dict[num_int])
        else:
            continue

    return decode_morse(''.join(decoded_word).replace("/", " "))