import socket
import code_unaire_chuck_norris
import charabia_latin
import chiffre_tritheme
import code_baudot
import otan
import leet_speak
import shankar
import accord_de_guitare_cipher
import code_wabun
import morbit
from time import sleep


# Adresse et port du serveur (à adapter si nécessaire)
HOST = 'localhost'
PORT = 12345

def solve_challenge():
    # Création du socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    data = client.recv(8192).decode().strip()
    print(f"\n{data}\n")

    for _ in range(100):
        # Réception de la chaîne encodée
        data = client.recv(2048).decode().strip()
        print(f"Received: \n{data}\n")
        
        if data.startswith("hint: ") or data.startswith("cipher: "):
            start = data.find("cipher: ")
            encoded_word = data[start + len("cipher: "):].strip()
            print(f"Encoded: {encoded_word}")
            
            if 'He can snap his toes' in data:
                # Traiter comme Chuck Norris encoding
                decoded_word = code_unaire_chuck_norris.chuck_norris_decode(encoded_word)
                print("chuck norris")
            
            elif "He can't imagine" in data:
                # Traiter comme Baudot encoding
                decoded_word = code_baudot.baudot_to_text(encoded_word).lower()
                print("baudot")

            elif '1337' in data:
                # Traiter comme Leet Speak
                decoded_word = leet_speak.leet_speak_decoder(encoded_word).lower()
                print("leet speak")
            
            elif all(c in 'Alfa Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliett Kilo Lima Mike November Oscar Papa Quebec Romeo Sierra Tango Uniform Victor Whiskey X-ray Yankee Zulu Zero One Two Three Four Five Six Seven Eight Nine'.split() for c in encoded_word.split()):
                # Traiter comme OTAN encoding
                decoded_word = otan.decode_from_phonetic(encoded_word).lower()
                print("otan")
                
            elif "charabia" in data:
                # Traiter comme Charabia Latin
                decoded_word = charabia_latin.charabia_latin_decoder(encoded_word)
                print("charabia latin")
            
            elif "slumdog" in data:
                # Traiter comme Shankar
                decoded_word = shankar.shankar_decrypt(encoded_word).lower()
                print("shankar")
            
            elif "Hendrix" in data:
                # Traiter comme Accord de Guitare
                decoded_word = accord_de_guitare_cipher.chords_to_word(encoded_word).lower()
                print("accord de guitare")
            elif "It looks like Morse code" in data:
                # Traiter comme Code Wabun
                decoded_word = code_wabun.decode_wabun(encoded_word)
                print("wabun")
            elif "AZERTYUO" in data:
                # Traiter comme Morbit encoding
                decoded_word = morbit.morbit_decoder(encoded_word).lower()
                print("morbit")
            else:
                # Traiter comme Chiffre de Trithème
                decoded_word = chiffre_tritheme.decode_chiffre_de_tritheme(encoded_word, 3)
                print("chiffre de tritheme")
            
            print(f"Test: {_}/100, decoded \"{decoded_word}\" \n\n")
            sleep(0.1)
            
            # Envoyer la chaîne déchiffrée
            client.send((decoded_word + "\n").encode())
        elif data.startswith("Wrong"):
            break
    
    # Lire le message final du serveur
    final_message = client.recv(2048).decode().strip()
    print(f"Server: {final_message}")

if __name__ == "__main__":
    solve_challenge()
