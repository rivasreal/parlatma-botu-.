import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# 7/24 Aktif tutmak için gerekli sistem
app = Flask('')
@app.route('/')
def home(): return "Bot Aktif!"
def run(): app.run(host='0.0.0.0', port=8000)
def keep_alive():
    t = Thread(target=run)
    t.start()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} Başlatıldı!')

@bot.command()
async def parlat(ctx):
    await ctx.send("✨ GEZGİN parlatma sistemi aktif!")

keep_alive()
# Aşağıdaki tırnak içine Discord Developer Portal'dan aldığın TOKENİ yapıştır!
bot.run('')
