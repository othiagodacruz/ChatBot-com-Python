# Arquivo com os comandos para interagir com o Telegram

import telebot
from .chaves import CHAVE_API_TELEGRAM
from .sistema import gerar_resposta
# importando as chaves e a função da resposta da IA

bot = telebot.TeleBot(CHAVE_API_TELEGRAM)   # Conectando com o Bot do Telegram

@bot.message_handler(commands=["start"])    # Define uma função básica /Start
def mensagem_boas_vindas(mensagem):
    bot.reply_to(mensagem, "Bem-vindo!")

@bot.message_handler(func=lambda m: True)   # Define o mais importante, uso da função de resposta da IA
def responder_mensagens(mensagem):          # chama a função e preenche com os dados das variaveis
    resposta = gerar_resposta(mensagem.text)
    bot.reply_to(mensagem, resposta)           # Envia a resposta no chat!

def iniciar_bot():                          # Inicia o BOT com essa função no MAIN.py
    print("Bot em funcionamento...")        # LOG de Inicialização
    bot.polling()