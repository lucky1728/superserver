import discord
from discord.ext import commands

#prefix
bot=commands.Bot(command_prefix='$')

#on_Ready
@bot.event
async def on_ready():
    print('Online')



#game_alert_commands


@bot.command()
async def l(ctx):
    if 'owner' in [i.name for i in ctx.message.author.roles]:
        await ctx.send(f'''@everyone **It's Loco Time!!**''')
        await ctx.send(f'''@everyone **It's Loco Time!!**''')
        await ctx.send(f'''@everyone **It's Loco Time!!**''')
        await ctx.send(f'''@everyone **It's Loco Time!!**''')

    else:
        await ctx.send('Lol You have no perms')


@bot.command()
async def q(ctx):
    if 'owner' in [i.name for i in ctx.message.author.roles]:
        await ctx.send(f'''@everyone **It's Qureka Time!!**''')
        await ctx.send(f'''@everyone **It's Qureka Time!!**''')
        await ctx.send(f'''@everyone **It's Qureka Time!!**''')
        await ctx.send(f'''@everyone **It's Qureka Time!!**''')

    else:
        await ctx.send('Lol You have no perms')

@bot.command()
async def b(ctx):
    if 'owner' in [i.name for i in ctx.message.author.roles]:
        await ctx.send(f'''@everyone **It's Baazinow Time!!**''')
        await ctx.send(f'''@everyone **It's Baazinow Time!!**''')
        await ctx.send(f'''@everyone **It's Baazinow Time!!**''')
        await ctx.send(f'''@everyone **It's Baazinow Time!!**''')

    else:
        await ctx.send('Lol You have no perms')


@bot.command()
async def h(ctx):
    if 'owner' in [i.name for i in ctx.message.author.roles]:
        await ctx.send(f'''@everyone **It's HQ Trivia Time!!**''')
        await ctx.send(f'''@everyone **It's HQ Trivia Time!!**''')
        await ctx.send(f'''@everyone **It's HQ Trivia Time!!**''')
        await ctx.send(f'''@everyone **It's HQ Trivia Time!!**''')

    else:
        await ctx.send('Lol You have no perms')



@bot.command()
async def t(ctx):
    if 'owner' in [i.name for i in ctx.message.author.roles]:
        await ctx.send(f'''@everyone **It's Trivaa Time!!**''')
        await ctx.send(f'''@everyone **It's Trivaa Time!!**''')
        await ctx.send(f'''@everyone **It's Trivaa Time!!**''')
        await ctx.send(f'''@everyone **It's Trivaa Time!!**''')

    else:
        await ctx.send('Lol You have no perms')



@bot.command()
async def sw(ctx):
    if 'owner' in [i.name for i in ctx.message.author.roles]:
        await ctx.send(f'''@everyone **It's Swag IQ Time!!**''')
        await ctx.send(f'''@everyone **It's Swag IQ Time!!**''')
        await ctx.send(f'''@everyone **It's Swag IQ Time!!**''')
        await ctx.send(f'''@everyone **It's Swag IQ Time!!**''')


    else:
        await ctx.send('Lol You have no perms')


@bot.command()
async def p(ctx):
    if 'owner' in [i.name for i in ctx.message.author.roles]:
        await ctx.send(f'''@everyone **It's PollBaazi Time!!**''')
        await ctx.send(f'''@everyone **It's PollBaazi Time!!**''')
        await ctx.send(f'''@everyone **It's PollBaazi Time!!**''')
        await ctx.send(f'''@everyone **It's PollBaazi Time!!**''')

    else:
        await ctx.send('Lol You have no perms')


@bot.command()
async def c(ctx):
    if 'owner' in [i.name for i in ctx.message.author.roles]:
        await ctx.send(f'''@everyone **It's Confetti Time!!**''')
        await ctx.send(f'''@everyone **It's Confetti Time!!**''')
        await ctx.send(f'''@everyone **It's Confetti Time!!**''')
        await ctx.send(f'''@everyone **It's Confetti Time!!**''')

    else:
        await ctx.send('Lol You have no perms')


@bot.command()
async def k(ctx):
    if 'owner' in [i.name for i in ctx.message.author.roles]:
        await ctx.send(f'''@everyone **It's My Karma Time!!**''')
        await ctx.send(f'''@everyone **It's My Karma Time!!**''')
        await ctx.send(f'''@everyone **It's My Karma Time!!**''')
        await ctx.send(f'''@everyone **It's My Karma Time!!**''')

    else:
        await ctx.send('Lol You have no perms')



@bot.command()
async def s(ctx):
    if 'owner' in [i.name for i in ctx.message.author.roles]:
        await ctx.send(f'''@everyone **It's Swoo Time!!**''')
        await ctx.send(f'''@everyone **It's Swoo Time!!**''')
        await ctx.send(f'''@everyone **It's Swoo Time!!**''')
        await ctx.send(f'''@everyone **It's Swoo Time!!**''')

    else:
        await ctx.send('Lol You have no perms')





#extra_commands


@bot.command(pass_context=True)
async def membercount(ctx):
    await ctx.send(f"No. Of members in this server are {ctx.message.guild.member_count}")


@bot.command()
async def pu(ctx,amount=1000):
    if 'owner' in [i.name for i in ctx.message.author.roles]:
        await ctx.channel.purge(limit=amount+1)

    else:
        await ctx.send('Lol You have no perms')





#accuracy_commands


@bot.command(pass_context=True)
async def ac(ctx,*,content):
    if 'owner' in [i.name for i in ctx.message.author.roles]:
        args=content.split(",")
        print(args)

        gamename = args[0]
        gametime = args[1]
        accuracy = args[2]



        embed=discord.Embed(
        title='Accuracy!',
        colour=discord.Colour.blue()
        )

        embed.set_footer(text='Made by Just for fun#4278||Super Trivia Official')
        embed.add_field(name='\u200b' , value=f'''GAME ------  {gamename}''' , inline=False)
        embed.add_field(name='\u200b' , value=f'''GAME TIME -----  {gametime}''' , inline=False)
        embed.add_field(name='\u200b' , value=f'''ACCURACY --------- {accuracy}''' , inline=False)
        embed.add_field(name='\u200b' , value=f'''I HOPE YOU ALL WON''' , inline = False)
        embed.set_image(url='https://media1.giphy.com/media/xULW8CPwOHXPua8NTa/source.gif')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/589042953067167744/589067316487127061/checkmark.gif')


        await ctx.send(embed=embed)
        await ctx.send('@everyone')

    else:
        await ctx.send('Lol You have no perms')



#announce_commands


@bot.command()
async def a(ctx,*,message):
    if 'owner' in [i.name for i in ctx.message.author.roles]:
        await ctx.send(message)

    else:
        await ctx.send('Lol You have no perms')



#token
bot.run('NTkyMzMwNDUzODczMzI4MTU5.XXOU8A.0PrMd94mLNpAbzwguulX1vqvuPM')
