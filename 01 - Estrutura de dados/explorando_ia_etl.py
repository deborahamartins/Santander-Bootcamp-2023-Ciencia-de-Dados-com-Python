# Objetivo: Usar o poder da IA Generativa para criar mensagens de marketing personalizadas que serão entregues a cada cliente.

sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

# Extrair lista de IDs de usuário a partir do arquivo CSV
import pandas as pd

df = pd.read_csv('SWD2023.csv')
user_ids = df['UserID'].to_list()
print(user_ids)

# Obter os dados de cada ID usando a API da Santander Dev Week 2023
import requests
import json

def get_user(id):
    response = requests.get(f'{sdw2023_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None

users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))

# Utilizar a API do OpenAI GPT-4 para gerar uma mensagem de marketing personalizada para cada usuário
openai_api_key = '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'

# Implementar a integração com o CHATGPT
import openai

openai.api_key = openai_api_key

def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system", 
                "content": "Vocé um especialista em marketing bancário."
            },
            {
                "role": "user", 
                "content": f"Crie uma mensagem para {user['name']} sobre a importância  dos investimentos (máximo de 100 caracteres)"
            }
        ]
    )
    return completion.choices[0].message.content.strip('\"')

for user in users:
    news = generate_ai_news(user)
    print(news)
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news
    })

# Atualizar a lista de "news" de cada usuário na API com a nova mensagem gerada
def update_user(user):
    response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False

for user in users:
    success = update_user(user)
print(f"User {user['name']} updated? {success}!")