curso = 'pYtHon'
# Maiúsculo
print(curso.upper())
# Minúsculo
print(curso.lower())
# Primeira letra maiúscula
print(curso.title())

curso = '    Python   '
# Remover espaços em branco na esquerda e na direita
print(curso.strip())
# Remover espaços em branco na esquerda
print(curso.lstrip())
# Remover espaços em branco na direita
print(curso.rstrip())

curso = 'Python'
# Centralização
print(curso.center(10, '#'))
print(curso.center(10))
# Junção
print('.'.join(curso))