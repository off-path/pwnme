def chiffre_de_tritheme(texte, decalage):
    resultat = []
    for i, char in enumerate(texte):
        if char.isalpha():
            # Calculer le décalage pour chaque caractère
            decalage_actuel = (decalage + i) % 26
            if char.islower():
                # Calculer le nouveau caractère pour les minuscules
                nouveau_char = chr((ord(char) - ord('a') + decalage_actuel) % 26 + ord('a'))
            else:
                # Calculer le nouveau caractère pour les majuscules
                nouveau_char = chr((ord(char) - ord('A') + decalage_actuel) % 26 + ord('A'))
            resultat.append(nouveau_char)
        else:
            resultat.append(char)  # Conserver les caractères non alphabétiques
    return ''.join(resultat)

def decode_chiffre_de_tritheme(texte, decalage):
    resultat = []
    for i, char in enumerate(texte):
        if char.isalpha():
            # Calculer le décalage pour chaque caractère
            decalage_actuel = (decalage + i) % 26
            if char.islower():
                # Calculer le nouveau caractère pour les minuscules
                nouveau_char = chr((ord(char) - ord('a') - decalage_actuel) % 26 + ord('a'))
            else:
                # Calculer le nouveau caractère pour les majuscules
                nouveau_char = chr((ord(char) - ord('A') - decalage_actuel) % 26 + ord('A'))
            resultat.append(nouveau_char)
        else:
            resultat.append(char)  # Conserver les caractères non alphabétiques
    return ''.join(resultat)

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
#     encoded = chiffre_de_tritheme(i)
#     decoded = decode_chiffre_de_tritheme(encoded)
#     if i != decoded:
#         print(f"Error:\n{i} -> {encoded} -> {decoded}")
#         error = True
#         break
# if not error: print("All tests passed")
