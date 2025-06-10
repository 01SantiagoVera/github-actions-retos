# main.py

def es_mayor_de_edad(edad):
    return edad >= 18

if __name__ == "__main__":
    edad = int(input("Ingresa tu edad: "))
    if es_mayor_de_edad(edad):
        print("✅ Eres mayor de edad.")
    else:
        print("❌ No eres mayor de edad.")

# main.py

def saludar(nombre):
    return f"Hola, {nombre}!"

if __name__ == "__main__":
    print(saludar("Santi"))
