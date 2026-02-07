def validar_numeros(a, b):
    es_a_un_numero = isinstance(a, (int, float))
    es_b_un_numero = isinstance(b, (int, float))
    return (es_a_un_numero and es_b_un_numero)
print("Buenas tardes")
def sumar(a, b, c):
    if not validar_numeros(a, b):
        return "Error: Solo se permiten números"
    resultado = a + b
    return resultado

def restar(a, b):
    if not validar_numeros(a, b):
        return "Error: Solo se permiten números"
    return a - b

def multiplicar(a, b):
    if not validar_numeros(a, b):
        return "Error: Solo se permiten números"
    return a * b

def dividir(a, b):
    if not validar_numeros(a, b):
        return "Error: Solo se permiten números"
    if b == 0:
        return "Error: División por cero"
    return a / b

def main():
    print("Calculadora básica")
    print("Operaciones disponibles: suma, resta, multiplicacion, division")
    op = input("Elige una operación: ").strip().lower()
    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
    except ValueError:
        print("Error: Debes ingresar solo números")
        return

    if op == "suma":
        resultado = sumar(a, b)
    elif op == "resta":
        resultado = restar(a, b)
    elif op == "multiplicacion":
        resultado = multiplicar(a, b)
    elif op == "division":
        resultado = dividir(a, b)
    else:
        resultado = "Operación no válida"

    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()