# main.py
import  os

def es_mayor_de_edad(edad):
    return edad >= 18

if __name__ == "__main__":

    if os.getenv("CI") == "true":
        edad=20
    else:
        edad=int(input("ingrese la edad"))

    if es_mayor_de_edad(edad):
        print("✅ Eres mayor de edad.")
    else:
        print("❌ No eres mayor de edad.")

# main.py

def saludar(nombre):
    return f"Hola, {nombre}!"

if __name__ == "__main__":
    print(saludar("Santi"))
