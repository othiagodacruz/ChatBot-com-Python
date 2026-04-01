# Arquivo responsável pela integração com a API da IA

import requests
import json
from .chaves import CHAVE_API_OPENROUTER
# Importa as chaves de API do arquivo chaves que haviam sido carregadas do .env

# Função para selecionar a IA desejada do OpenRouter, enviar a mensagem p/ a IA e retornar a resposta
def gerar_resposta(mensagem_usuario):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {CHAVE_API_OPENROUTER}",
            "Content-Type": "application/json"
        },

# Até aqui foi autorizado e definido o uso da API no site da OpenRouter

        json={
            "model": "google/gemma-3n-e4b-it:free",         # Modelo a ser usado (pode ser substituido!)
            "messages": [
                {"role": "user", "content": mensagem_usuario}   # Lista com a Mensagem que a IA vai receber
            ]
        }
    )

# Até aqui foi selecionada a IA desejada (Gratuita) para o ChatBot

    print("STATUS:", response.status_code)      # Teste de Status
    print("RESPOSTA:", response.text)           # Teste de Resposta

# Os testes acima são para manutenção!

    if response.status_code != 200:
        return "Erro na API da IA."       # "ChatBot" retorna o erro no chat
    
    dados = response.json()

    if "choices" in dados:
        return dados["choices"][0]["message"]["content"]
    
# If para retornar a resposta da IA te respondendo no ChatBot
    
    return "Erro de sistema ao gerar resposta."    # Caso o erro seja do sistema e não da própria IA