import re

def password_policy_check(username, password):
    # Minimálně 10 znaků.
    if len(password) < 10:
        return False
    
    # Jedno číslo.
    if not re.search(r'\d', password):
        return False
    
    # Heslo musí obsahovat alespoň jedno písmeno malé a jedno písmeno velké abecedy.
    if not (re.search(r'[a-z]', password) and re.search(r'[A-Z]', password)):
        return False
    
    # Nečíselný a nepísmený znak.
    if not re.search(r'\W', password):
        return False
    
    # Neobsahuje username.
    if username.lower() in password.lower():
        return False
    
    # Neobsahujepodřetězec username delší než 3 znaky.
    for i in range(len(username) - 2):
        substring = username[i:i+3]
        if substring.lower() in password.lower():
            return False
    return True

username = "Dominik"
password = "husak2"
if password_policy_check(username, password):
    print("Heslo je platné.")
else:
    print("Heslo není platné.")