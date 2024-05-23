# Dictionnaire de correspondance des lettres aux accords de guitare
chords_dict = {
    'A': 'x02220',
    'B': 'x24442',
    'C': 'x32010',
    'D': 'xx0232',
    'E': '022100',
    'F': '133211',
    'G': '320003'
}

def word_to_chords(word):
    # Convertir chaque lettre du mot en accord
    chords = [chords_dict[letter.upper()] for letter in word if letter.upper() in chords_dict]
    # Joindre les accords avec des espaces
    return ' '.join(chords)

def chords_to_word(chords):
    # Inverser le dictionnaire pour correspondance des accords aux lettres
    inverse_chords_dict = {v: k for k, v in chords_dict.items()}
    
    # Diviser la chaîne d'accords en une liste d'accords
    chords_list = chords.split()
    
    # Convertir chaque accord en lettre
    word = ''.join([inverse_chords_dict[chord] for chord in chords_list if chord in inverse_chords_dict])
    
    return word

# Test
# words_guitar = ["decade", "deface", "degage", "badged", "baffed", "beaded", "bedded"]
# error = False

# for i in words_guitar:
#     encoded = word_to_chords(i)
#     decoded = chords_to_word(encoded)
#     if i != decoded:
#         print(f"Error:\n{i} -> {encoded} -> {decoded}")
#         error = True
#         break
# if not error: print("All tests passed")
