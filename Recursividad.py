#EJERCICIO 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Ingrese un número: "))

for i in range(1, n + 1):
    print(f"Factorial de {i} = {factorial(i)}")

#EJERCICIO 2
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

pos = int(input("Ingrese la posición hasta donde quiere ver la serie: "))

print("Serie de Fibonacci:")
for i in range(pos + 1):
    print(fibonacci(i), end=" ")

#EJERCICIO 3
def potencia(n, m):
    if m == 0:
        return 1
    return n * potencia(n, m - 1)

base = int(input("Ingrese la base: "))
exp = int(input("Ingrese el exponente: "))

resultado = potencia(base, exp)
print(f"{base} elevado a {exp} = {resultado}")

#EJERCICIO 4
def decimal_a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("Ingrese un número entero en base decimal: "))
print("Representación binaria:", decimal_a_binario(num))

#EJERCICIO 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra (sin espacios ni tildes): ")
print("¿Es palíndromo?:", es_palindromo(texto))

#EJERCICIO 6
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un número entero positivo: "))
print("Suma de sus dígitos =", suma_digitos(numero))

#EJERCICIO 7
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

niveles = int(input("Ingrese el número de bloques en el nivel inferior: "))
print("Bloques totales necesarios:", contar_bloques(niveles))

#EJERCICIO 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

num = int(input("Ingrese un número entero positivo: "))
dig = int(input("Ingrese el dígito a buscar (0-9): "))
print("Cantidad de veces que aparece:", contar_digito(num, dig))

#FIN DEL ARCHIVO
