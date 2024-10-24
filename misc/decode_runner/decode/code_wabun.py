# Dictionnaire complet du Code Wabun pour les syllabes japonaises
alphabet = "a, i, u, e, o, ka, ki, ku, ke, ko, sa, shi, su, se, so, ta, chi, tsu, te, to, na, ni, nu, ne, no, ha, hi, fu, he, ho, ma, mi, mu, me, mo, ya, yu, yo, ra, ri, ru, re, ro, wa, wi, n, we, wo, kya, kyu, kyo, sha, shu, sho, cha, chu, cho, nya, nyu, nyo, hya, hyu, hyo, mya, myu, myo, rya, ryu, ryo, ga, gi, gu, ge, go, gya, gyu, gyo, za, ji, zu, ze, zo, ja, ju, jo, da, ji, zu, de, do, ja, ju, jo, ba, bi, bu, be, bo, bya, byu, byo, pa, pi, pu, pe, po, pya, pyu, pyo"
alphabet_wabun = alphabet.split(", ")

code = "--.--   .-   ..-   -.---   .-...   .-..   -.-..   ...-   -.--   ----   -.-.-   --.-.   ---.-   .---.   ---.   -.   ..-.   .--.   .-.--   ..-..   .-.   -.-.   ....   --.-   ..--   -...   --..-   --..   .   -..   -..-   ..-.-   -   -...-   -..-.   .--   -..--   --   ...   --.   -.--.   ---   .-.-   -.-   .-..-   .-.-.   .--..   .---   -.-.. .--   -.-.. -..--   -.-.. --   --.-. .--   --.-. -..--   --.-. --   ..-. .--   ..-. -..--   ..-. --   -.-. .--   -.-. -..--   -.-. --   --..- .--   --..- -..--   --..- --   ..-.- .--   ..-.- -..--   ..-.- --   --. .--   --. -..--   --. --   .-.. ..   -.-.. ..   ...- ..   -.-- ..   ---- ..   -.-.. .. .--   -.-.. .. -..--   -.-.. .. --   -.-.- ..   ..-. ..   .--. ..   .---. ..   ---. ..   ..-. .. .--   ..-. .. -..--   ..-. .. --   -. ..   ..-. ..   .--. ..   .-.-- ..   ..-.. ..   ..-. .. .--   ..-. .. -..--   ..-. .. --   -... ..   --..- ..   --.. ..   . ..   -.. ..   --..- .. .--   --..- .. -..--   --..- .. --   -... ..--.   --..- ..--.   --.. ..--.   . ..--.   -.. ..--.   --..- ..--. .--   --..- ..--. -..--   P --"
code_wabun = code.split("   ")

wabun_code = dict(zip(alphabet_wabun, code_wabun))


def decode_wabun(encoded_text):
    inverse_wabun_code = {v: k for k, v in wabun_code.items()}
    decoded_text = []
    codes = encoded_text.split()
    for code in codes:
        if code in inverse_wabun_code:
            decoded_text.append(inverse_wabun_code[code])
        else:
            decoded_text.append(code)  # code non reconnu, renvoyé en clair
    return ''.join(decoded_text)