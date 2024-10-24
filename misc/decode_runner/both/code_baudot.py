# Table de conversion pour les lettres (Lettres)
baudot_letters = {
    'A': '00011', 'B': '11001', 'C': '01110', 'D': '01001', 'E': '00001', 'F': '01101',
    'G': '11010', 'H': '10100', 'I': '00110', 'J': '01011', 'K': '01111', 'L': '10010',
    'M': '11100', 'N': '01100', 'O': '11000', 'P': '10110', 'Q': '10111', 'R': '01010',
    'S': '00101', 'T': '10000', 'U': '00111', 'V': '11110', 'W': '10011', 'X': '11101',
    'Y': '10101', 'Z': '10001', ' ': '00100'
}

# Table de conversion pour les chiffres et les symboles (Figures)
baudot_figures = {
    '1': '00011', '2': '11001', '3': '01110', '4': '01001', '5': '00001', '6': '01101',
    '7': '11010', '8': '10100', '9': '00110', '0': '01011', '-': '01111', '!': '10010',
    '&': '11100', '#': '01100', "'": '11000', '(': '10110', ')': '10111', '"': '01010',
    '/': '00101', ':': '10000', ';': '00111', '?': '11110', ',': '10011', '.': '11101',
    '+': '10101', '=': '10001', ' ': '00100'
}

# Fonction pour convertir une chaîne de caractères en code Baudot
def text_to_baudot(text):
    mode = 'letters'  # Mode initial: Lettres
    result = []

    for char in text.upper():
        if char in baudot_letters:
            if mode == 'figures':
                result.append('11111')  # Passer en mode Lettres
                mode = 'letters'
            result.append(baudot_letters[char])
        elif char in baudot_figures:
            if mode == 'letters':
                result.append('11011')  # Passer en mode Figures
                mode = 'figures'
            result.append(baudot_figures[char])
        else:
            raise ValueError(f"Caractère non supporté: {char}")

    return ' '.join(result)

def baudot_to_text(baudot_code):
    baudot_symbols = baudot_code.split()
    mode = 'letters'  # Mode initial: Lettres
    result = []

    for symbol in baudot_symbols:
        if symbol == '11111':  # Changer en mode Lettres
            mode = 'letters'
        elif symbol == '11011':  # Changer en mode Figures
            mode = 'figures'
        else:
            if mode == 'letters':
                baudot_letters_inverse = {v: k for k, v in baudot_letters.items()}
                result.append(baudot_letters_inverse.get(symbol, '?'))
            elif mode == 'figures':
                baudot_figures_inverse = {v: k for k, v in baudot_figures.items()}
                result.append(baudot_figures_inverse.get(symbol, '?'))

    return ''.join(result)



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
#     encoded = text_to_baudot(i)
#     decoded = baudot_to_text(encoded)
#     if i != decoded:
#         print(f"Error:\n{i} -> {encoded} -> {decoded}")
#         error = True
#         break
# if not error: print("All tests passed")


