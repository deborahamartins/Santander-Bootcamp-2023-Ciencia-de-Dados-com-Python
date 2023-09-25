texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=' ')
print() 


# Range com for
for numero in range(0, 11):
    print(numero, end=' ')

for numero in range(0, 51, 5):
    print(numero, end=' ')


opcao = -1

