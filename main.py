import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Dan inilah cara Kamu mengganti nama file dari variabel!

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

organik = ["daun","sayur","kulit pisang ambon"]
anorganik = ["plastik","besi","kabel"]

# @bot.command()
# async def pilih(ctx, *sampah):
#     temp = " ".join(sampah)
#     if temp in organik:
#         await ctx.send("Masukkan dalam sampah organik")
#     elif temp in anorganik:
#         await ctx.send("Masukkan dalam sampah anorganik")

@bot.command()
async def pilih(ctx):
    await ctx.send('Masukkan sampah')

    msg = await bot.wait_for("message")

    if msg.content in organik:
        await ctx.send("Masukkan dalam organik")
    else:
        await ctx.send("Masukkan dalam anorganik")

bot.run("MASUKKAN TOKEN DI SINI")
