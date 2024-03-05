import random

import discord

from discord.ext import commands

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event

async def on_ready():

    print(f'{bot.user} olarak giriş yaptık')

@bot.command()

async def hello(ctx):

    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()

async def heh(ctx, count_heh = 5):

    if count_heh > 1000:

        await ctx.send("Yok Daha Neler")

    else:

        await ctx.send("he"* count_heh)

@bot.command()

async def gunduz(ctx,a):

    await ctx.send("Merhaba Gündüz" * int(a) )

@bot.command()

async def tesekkur(ctx,a):

    await ctx.send("Bir Şey Değil" * int(a) )
@bot.command()
async def hey(ctx,a):

    await ctx.send("ne" * int(a) )
    
@bot.command()
async def hey(ctx,a):

    await ctx.send("ne" * int(a) )

@bot.command()
async def antalya(ctx,a):

    await ctx.send("Konyaaltı'nda doğdum" * int(a) )
    
@bot.command()
async def turkiye(ctx,a):

    await ctx.send("81 ili vardır.Antalya'da doğdum" * int(a) )

@bot.command()
async def dunya(ctx,a):

    await ctx.send("195 ülkesi vardır.Türkiye'de doğdum" * int(a) )


bot.run("")
