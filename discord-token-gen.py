import random
import string
import json

def generer_tokens(n):
    """Génère n tokens aléatoires avec les préfixes MT, NT, et MD et les retourne sous forme de liste"""
    tokens = [] # Liste pour stocker les tokens générés
    prefixes = ["MT", "NT", "MD"] # Liste des préfixes disponibles
    for _ in range(n): # Boucle pour générer n tokens
        # Choisir un préfixe aléatoirement
        prefix = random.choice(prefixes)
        # Génère un token aléatoire en concaténant le préfixe et plusieurs chaînes de caractères aléatoires
        token = prefix
        token += random.choice(string.ascii_letters)
        token += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))
        token += "."
        token += random.choice(string.ascii_letters).upper()
        token += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
        token += "."
        token += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
        tokens.append(token)          
        
    return tokens

# Demander à l'utilisateur combien de tokens il souhaite générer
n = int(input("Combien de tokens veux-tu générer ? "))

# Générer les tokens et afficher le résultat
tokens = generer_tokens(n)

# Export en .json le résultat
with open('tokens.json', 'w') as f:
    json.dump(tokens, f)
