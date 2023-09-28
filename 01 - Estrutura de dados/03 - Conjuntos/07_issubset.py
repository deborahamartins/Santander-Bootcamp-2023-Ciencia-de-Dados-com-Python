conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# Todos os elementos de A estão em B
resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

# Todos os elementos de B estão em A
resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)