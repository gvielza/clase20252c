

def leer_cadena(cadena):
    
    if any(c.isupper() for c in cadena) and any(c.islower() for c in cadena):
        return True
    else:
        return False