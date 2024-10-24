# Alphabets définis selon la substitution de Shankar
original_alphabet = "DFGHJKLMNUOPQRSTIVWXYZBACE"
shankar_alphabet = "XWYAZBCDQEFGHIKLMNOPJRSTUV"

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