while True:
    
    try:
        puerto = int(input("Ingrese un numero de puerto: "))
        if 0 <= puerto <= 1023:
            print("Puerto bien conocido: 0-1023 ")
        elif 1024 <= puerto <= 49151:
            print("Puerto registrado: 1024- 49151")
        elif 49151 <= puerto <= 65535:
            print("Puerto Dinamicó o Privado: 49152-65535")
        else:
            print("Número fuera del rango válido de puertos.")
    except ValueError:
        print("Ingrese un numero de puerto valido") 
        