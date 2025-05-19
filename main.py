import os
import requests
import telebot

API_TOKEN = os.getenv("API_TOKEN")  # Coloque a variável de ambiente no Render
API_FOOTBALL_KEY = os.getenv("FOOTBALL_API_KEY")  # Coloque também no Render
bot = telebot.TeleBot(API_TOKEN)

HEADERS = {
    "x-apisports-key": API_FOOTBALL_KEY
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Olá! Envie /ao_vivo para ver os jogos de hoje ao vivo.")

@bot.message_handler(commands=['ao_vivo'])
def ao_vivo(message):
    url = "https://v3.football.api-sports.io/fixtures?live=all"
    response = requests.get(url, headers=HEADERS)
    data = response.json()

    if data['response']:
        resposta = ""
        for jogo in data['response'][:5]:  # mostra até 5 jogos ao vivo
            times = jogo['teams']
            placar = jogo['goals']
            resposta += f"{times['home']['name']} {placar['home']} x {placar['away']} {times['away']['name']}\n"
        bot.send_message(message.chat.id, resposta)
    else:
        bot.send_message(message.chat.id, "Nenhum jogo ao vivo agora.")

# Você pode adicionar mais comandos depois, como /palpites ou /estatisticas

bot.polling()
