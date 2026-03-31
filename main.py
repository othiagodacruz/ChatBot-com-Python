import telebot
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

CHAVE_API_TELEGRAM = os.getenv("TOKEN_TELEGRAM")
CHAVE_API_OPENROUTER = os.getenv("OPENROUTER_TOKEN")

if not CHAVE_API_TELEGRAM:
    print("Chave da API do Telegram não encontrada!")
    exit()

if not CHAVE_API_OPENROUTER:
    print("Chave da API do OpenRouter não encontrada!")
    exit()

bot = telebot.TeleBot(CHAVE_API_TELEGRAM)

@bot.message_handler(commands=["start"])
def mensagem_boas_vindas(mensagem):
    bot.reply_to(mensagem, text="Bem Vindo!")

@bot.message_handler(func=lambda m: True)
def responder_mensagens(mensagem):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer " + CHAVE_API_OPENROUTER,
        },
        data=json.dumps({
            "model": "google/gemma-3n-e2b-it:free",
            "messages": [
            {
                "role": "user",
                "content": mensagem.text
            }
            ]
        })
    )
    dados = response.json()
    if "choices" in dados:
        texto_da_ia = dados["choices"][0]["message"]["content"]
        bot.reply_to(mensagem, texto_da_ia)
    else:
        print("Erro na resposta", dados)

print("Bot em funcionamento...")

bot.polling()