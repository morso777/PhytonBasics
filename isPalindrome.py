# Leer entrada
A = input()

# Verificar si es palíndromo comparando con su reverso
if A == A[::-1]:
    print("Yes")
else:
    print("No")
