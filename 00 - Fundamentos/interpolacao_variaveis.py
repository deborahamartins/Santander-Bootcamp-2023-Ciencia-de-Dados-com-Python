nome = 'Déborah'
idade = 22
profissao = 'Analista de Dados'
linguagem = 'Python'
# Old style %
print('Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no cruso de %s'% (nome, idade, profissao, linguagem))

# Método format
print('Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no cruso de {}' .format(nome, idade, profissao, linguagem))

print('Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no cruso de {0}' .format(linguagem, profissao, idade, nome))

print('Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no cruso de {linguagem}' .format(nome = nome, idade = idade, profissao = profissao, linguagem = linguagem))

#print('Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no cruso de {linguagem}' .format(**pessoa))

# f-string
print(f'Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.')

# Formatar strings com f-string
PI = 3.14159
print(f'Valor de PI: {PI:.2f}')
# 10 espaços em branco
print(f'Valor de PI: {PI:10.2f}')