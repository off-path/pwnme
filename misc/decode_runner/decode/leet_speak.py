leet_dict = {
        'A': '4', 'B': '8', 'C': 'C', 'D': 'D', 'E': '3', 'F': 'F', 'G': '6', 'H': 'H', 'I': '1', 'J': 'J',
        'K': '|<', 'L': '1', 'M': 'M', 'N': 'N', 'O': '0', 'P': 'P', 'Q': 'Q', 'R': 'r', 'S': '5', 'T': '7',
        'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'
    }

def leet_speak_decoder(text):


    # Create an inverse dictionary for decoding
    inverse_leet_dict = {v: k for k, v in leet_dict.items()}

    # Decode the text from leet speak
    decoded_text = ''
    i = 0
    while i < len(text):
        match_found = False
        # Check for multi-character mappings first
        for length in range(4, 0, -1):  # Longest to shortest
            if i + length <= len(text) and text[i:i + length] in inverse_leet_dict:
                decoded_text += inverse_leet_dict[text[i:i + length]]
                i += length
                match_found = True
                break
        if not match_found:
            decoded_text += text[i]
            i += 1

    return decoded_text