"""
1. Pedir al usuario dos números enteros.
2. Mostrar un menú con las opciones: sumar, restar, multiplicar, dividir.
3. Según la opción elegida, realizar la operación correspondiente.
4. Mostrar el resultado.
"""

numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))

print("Seleccione una operación a realizar")
print("Sus opciones son las siguientes: ")
print("Suma: +")
print("Resta: -")
print("Multiplicación: *")
print("División: /")
operacion = input("Ingrese el simbolo de la operación a realizar: ")

if operacion == "+":
    print(f"Resultado: {numero_1 + numero_2}")
elif operacion == "-":
    print(f"Resultado: {numero_1 - numero_2}")
elif operacion == "*":
    print(f"Resultado: {numero_1 * numero_2}")
# ...existing code...
elif operacion == "/":
    if numero_2 == 0:
        print("Error: No se puede dividir por cero.")
    else:
        print(f"Resultado: {numero_1 / numero_2}")
# ...existing code...
else:
    print("La operacion ingresada no es valida")

# numero_1 = None
# numero_2 = None

# def pedir_numeros():
#     pass


# def mostrar_menu():
#     pass


# def suma():
#     pass


# def resta():
#     pass


# def multi():
#     pass


# def division():
#     pass
