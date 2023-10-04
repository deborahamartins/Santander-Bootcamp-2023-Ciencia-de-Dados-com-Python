import pandas as pd
import sqlite3

# Extração - Carregar dados do arquivo CSV
column_names = ['nome', 'Nota1', 'Nota2', 'Nota3']
df = pd.read_csv('alunos.csv', names=column_names, header=0)

# Transformação - Calcular a média e a situação do aluno
df['Média'] = df[['Nota1', 'Nota2', 'Nota3']].mean(axis=1).round(2)
df['Situação'] = df['Média'].apply(lambda x: 'Aprovado' if x >= 6 else 'Reprovado')

# Carregamento - Criar um banco de dados SQLite e carregar os dados
conn = sqlite3.connect('escola.db')
df.to_sql('alunos', conn, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados
conn.close()

# Verificar banco
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM alunos;")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()