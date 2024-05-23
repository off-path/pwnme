# Alphabets définis selon la substitution de Shankar
original_alphabet = "DFGHJKLMNUOPQRSTIVWXYZBACE"
shankar_alphabet = "XWYAZBCDQEFGHIKLMNOPJRSTUV"


def shankar_encrypt(text):

    """Chiffre un texte en utilisant l'alphabet de Shankar."""
    encrypt_dict = {original_alphabet[i]: shankar_alphabet[i] for i in range(len(original_alphabet))}
    encrypted_text = ""
    for char in text.upper():
        if char in encrypt_dict:
            encrypted_text += encrypt_dict[char]
        else:
            encrypted_text += char  # Pour conserver les caractères non alphabétiques
    return encrypted_text

def shankar_decrypt(text):
    """Déchiffre un texte en utilisant l'alphabet de Shankar."""
    decrypt_dict = {shankar_alphabet[i]: original_alphabet[i] for i in range(len(original_alphabet))}
    decrypted_text = ""
    for char in text.upper():
        if char in decrypt_dict:
            decrypted_text += decrypt_dict[char]
        else:
            decrypted_text += char  # Pour conserver les caractères non alphabétiques
    return decrypted_text

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
#     encoded = shankar_encrypt(i)
#     decoded = shankar_decrypt(encoded)
#     if i != decoded:
#         print(f"Error:\n{i} -> {encoded} -> {decoded}")
#         error = True
#         break
# if not error: print("All tests passed")
