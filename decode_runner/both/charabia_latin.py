import random

def charabia_latin_encoder(word):
    # Inverser le mot
    reversed_word = word[::-1]
    # Choisir une terminaison aléatoire
    ending = random.choice(['us', 'um', 'it'])
    # Ajouter la terminaison à la fin
    encoded_word = reversed_word + ending
    return encoded_word

def charabia_latin_decoder(encoded_word):
    # Vérifier et supprimer la terminaison
    if encoded_word.endswith("us"):
        core_word = encoded_word[:-2]
    elif encoded_word.endswith("um"):
        core_word = encoded_word[:-2]
    elif encoded_word.endswith("it"):
        core_word = encoded_word[:-2]
    else:
        raise ValueError("Mot encodé avec une terminaison invalide.")
    
    # Inverser le mot pour obtenir l'original
    decoded_word = core_word[::-1]
    return decoded_word

# Test 
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
#     encoded = charabia_latin_decoder(i)
#     decoded = charabia_latin_decoder(encoded)
#     if i != decoded:
#         print(f"Error:\n{i} -> {encoded} -> {decoded}")
#         error = True
#         break
# if not error: print("All tests passed")