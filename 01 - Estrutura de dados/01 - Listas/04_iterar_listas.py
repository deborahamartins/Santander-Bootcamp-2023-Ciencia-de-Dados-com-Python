carros = ["gol", "celta", "palio"]
# Acessar cada item
for carro in carros:
    print(carro)

# Função enumerate
for indice, carro in enumerate(carros):
    print(f"{indice} - {carro}")