def chuck_norris_encode(message):
    binary_message = ''.join(f'{ord(c):07b}' for c in message)  # Convertir chaque caractère en binaire de 7 bits
    encoded_message = []
    
    i = 0
    while i < len(binary_message):
        bit = binary_message[i]
        count = 1
        while i + 1 < len(binary_message) and binary_message[i + 1] == bit:
            count += 1
            i += 1
        if bit == '1':
            encoded_message.append('0 ' + '0' * count)
        else:
            encoded_message.append('00 ' + '0' * count)
        i += 1
    
    return ' '.join(encoded_message)

def chuck_norris_decode(encoded_message):
    parts = encoded_message.split()
    binary_message = ''
    i = 0
    while i < len(parts):
        prefix = parts[i]
        zero_block = parts[i + 1]
        if prefix == '0':
            binary_message += '1' * len(zero_block)
        elif prefix == '00':
            binary_message += '0' * len(zero_block)
        i += 2
    
    chars = [binary_message[j:j + 7] for j in range(0, len(binary_message), 7)]
    return ''.join([chr(int(c, 2)) for c in chars])

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
#     encoded = chuck_norris_encode(i)
#     decoded = chuck_norris_decode(encoded)
#     if i != decoded:
#         print(f"Error:\n{i} -> {encoded} -> {decoded}")
#         error = True
#         break
# if not error: print("All tests passed")

