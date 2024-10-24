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