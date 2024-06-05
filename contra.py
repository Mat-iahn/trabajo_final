def verificar_contraseña(contraseña):
  
    if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return False
    
    if not any(char.isupper() for char in contraseña):
        print("La contraseña debe tener al menos una letra mayúscula.")
        return False
    
    if not any(char.isdigit() for char in contraseña):
        print("La contraseña debe tener al menos un número.")
        return False
    
    print("La contraseña es válida.")
    return True

def solicitar_contraseña():
    while True:
        contraseña = input("Por favor, ingrese una contraseña: ")
        if verificar_contraseña(contraseña):
            break

solicitar_contraseña()