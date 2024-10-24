chords_dict = {
    'A': 'x02220',
    'B': 'x24442',
    'C': 'x32010',
    'D': 'xx0232',
    'E': '022100',
    'F': '133211',
    'G': '320003'
}

def chords_to_word(chords):
    # Inverser le dictionnaire pour correspondance des accords aux lettres
    inverse_chords_dict = {v: k for k, v in chords_dict.items()}
    
    # Diviser la chaîne d'accords en une liste d'accords
    chords_list = chords.split()
    
    # Convertir chaque accord en lettre
    word = ''.join([inverse_chords_dict[chord] for chord in chords_list if chord in inverse_chords_dict])
    
    return word