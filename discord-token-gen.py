"""Update by https://github.com/Ybucaille"""

import random
import string

def generer_tokens(n):
    """Génère n tokens aléatoires avec les préfixes MT, NT, et MD et les retourne sous forme de liste"""
    tokens = []  # Initialise la liste des tokens
    prefixes = ["MT", "NT", "MD"]  # Liste des préfixes disponibles
    for _ in range(n):  # Boucle pour générer n tokens
        # Génère un token aléatoire en concaténant le préfixe et plusieurs chaînes de caractères aléatoires
        token = "".join([
            random.choice(prefixes),
            random.choice(string.ascii_letters),
            ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21)),
            ".",
            random.choice(string.ascii_letters).upper(),
            ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5)),
            ".",
            ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27)),
        ])
        # Ajoute le token à la liste
        tokens.append(token)
    return tokens


# Demander à l'utilisateur combien de tokens il souhaite générer
n = int(input("Combien de tokens veux-tu générer ? "))

# Générer les tokens
tokens = generer_tokens(n)

# Ouvrir le fichier en mode écriture
with open("tokens.txt", "w") as f:
    # Écrire chaque token sur une nouvelle ligne
    for token in tokens:
        f.write(token + "\n")
