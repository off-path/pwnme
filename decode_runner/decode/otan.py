# Dictionnaire de l'alphabet phonétique de l'OTAN
phonetic_alphabet = {
    'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
    'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
    'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
    'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
    'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
    'Y': 'Yankee', 'Z': 'Zulu', '0': 'Zero', '1': 'One',
    '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
    '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
}

def decode_from_phonetic(phonetic_text):
    reverse_phonetic_alphabet = {value: key for key, value in phonetic_alphabet.items()}
    words = phonetic_text.split()
    decoded_text = []
    
    for word in words:
        if word in reverse_phonetic_alphabet:
            decoded_text.append(reverse_phonetic_alphabet[word])
        else:
            decoded_text.append(word)  # Garder les mots non-reconnus tels quels
    
    return ''.join(decoded_text)