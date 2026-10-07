def est_palindrome(texte):
    texte = texte.replace(" ", "").lower()
    return texte == texte[::-1]