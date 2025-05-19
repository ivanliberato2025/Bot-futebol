import telebot
import requests
import os

TOKEN = os.getenv("API_TOKEN")
API_KEY = os.getenv("API_FOOTBALL_KEY")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "Olá! Envie o nome de um time que eu te dou informações da próxima partida!")

@bot.message_handler(func=lambda m: True)
def responder(msg):
    time = msg.text
    url = f"https://v3.football.api-sports.io/teams?search={time}"
    headers = {"x-apisports-key": API_KEY}
    r = requests.get(url, headers=headers).json()

    if r['results'] == 0:
        bot.reply_to(msg, "Time não encontrado.")
        return

    team_id = r['response'][0]['team']['id']
    r2 = requests.get(f"https://v3.football.api-sports.io/fixtures?team={team_id}&next=1", headers=headers).json()

    if r2['results'] == 0:
        bot.reply_to(msg, "Sem jogos encontrados.")
        return

    jogo = r2['response'][0]
    adversario = jogo['teams']['away']['name'] if jogo['teams']['home']['id'] == team_id else jogo['teams']['home']['name']
    data = jogo['fixture']['date'][:10]
    bot.reply_to(msg, f"Próximo jogo contra: {adversario} na data: {data}")

bot.polling()
