leet_dict = {
        'A': '4', 'B': '8', 'C': 'C', 'D': 'D', 'E': '3', 'F': 'F', 'G': '6', 'H': 'H', 'I': '1', 'J': 'J',
        'K': '|<', 'L': '1', 'M': 'M', 'N': 'N', 'O': '0', 'P': 'P', 'Q': 'Q', 'R': 'r', 'S': '5', 'T': '7',
        'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'
    }


def leet_speak_encoder(text):
    
    # Convert the text to uppercase to match the leet dictionary keys
    text = text.upper()

    # Encode the text into leet speak
    encoded_text = ''
    for char in text:
        if char in leet_dict:
            encoded_text += leet_dict[char]
        else:
            encoded_text += char

    return encoded_text

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

# Tests
# words = [
#     "abeille", "baleine", "camion", "danser", "elephant", "fromage", "grenouille", 
#     "hamster", "igloo", "jardin", "kangourou", "lampe", "magicien", "nager", 
#     "oiseau", "parapluie", "quiche", "robot", "serpent", "tigre", "uniforme", 
#     "vampire", "wagon", "xylophone", "yoga", "zebre", "avion", "brouette", 
#     "crocodile", "diamant", "ecureuil", "fleur", "guitare", "hippopotame", 
#     "insecte", "jambon", "klaxon", "loutre", "moustache", "navire", "ordinateur", 
#     "pizza", "quatre", "requin", "singe", "tomate", "ustensile", "vent", 
#     "walrus", "xylophone", "yeti", "zoo", "arc", "banane", "chien", "dauphin", 
#     "echelle", "fenetre", "gateau", "horloge", "iguanodon", "jasmin", "koala", 
#     "libellule", "maison", "noix", "orange", "panthere", "question", "raton", 
#     "souris", "tortue", "univers", "violon", "wagonnet", "xylocope", "yaourt", 
#     "zinc", "ananas", "bison", "clown", "dragon", "escargot", "fusil", "girafe", 
#     "huitre", "internet", "jouet", "kiwi", "loup", "moto", "ninja", "oiselet", 
#     "parc", "quartz", "riviere", "souris", "tuba", "usine", "vanille", "wagon"
# ]
# error = False

# for i in words:
#     encoded = leet_speak_encoder(i)
#     decoded = leet_speak_decoder(encoded)
#     if i != decoded:
#         print(f"Error:\n{i} -> {encoded} -> {decoded}")
#         error = True
#         break
# if not error: print("All tests passed")
