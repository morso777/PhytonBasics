# Leer la entrada
A = input()

# Usar reversed() y unir los caracteres con join
reversed_A = ''.join(reversed(A))

# Comparar la cadena original con la invertida
if A == reversed_A:
    print("Yes")
else:
    print("No")