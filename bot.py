import discord
import os
from dotenv import load_dotenv
from discord.commands import Option

bot = discord.Bot()
load_dotenv()

@bot.event
async def on_ready():
    print(f'{bot.user} connect success!')


@bot.slash_command(description="Site is trancelate")
async def site_trancelate(
    ctx,
    url: Option(str, 'want to trancelate link typing'),
    input: Option(str, 'before trancelate language(example: auto, jp) ※details /help command.'),
    output: Option(str, 'after trancelate language(example: en, th) ※details /help command.'),
):
    link = ' '

    if url[0:8] == 'https://' or url[0:7] == 'http://':
        # debug message start
        print('-Generate start-')
        print('')

        link = 'https://translate.google.com/translate?sl=' + input + '&tl=' + output + '&u=' + url 
        print(link)
        print('')

        print('-Generate finish!-')
        print('')
        # debug message finish

        embed=discord.Embed(title="Success!", description=":o:Generate URL!:o:", color=0x00ff2a)
        embed.add_field(name="This is link !", value=link, inline=True)
        await ctx.respond(embed=embed)
    # Error message
    else:
        # debug message start
        print('-Generate start!-')
        print('')

        print('Error!')
        print('')

        print('-Generate finish!-')
        print('')
        # debug message finish

        embed=discord.Embed(title="Error!", description=":x:No Link!:x:", color=0xff0000)
        await ctx.respond(embed=embed)
        # https://ai-inter1.com/python-if-andor/

@bot.slash_command(description="command help.")
async def help(ctx):
    embed=discord.Embed(title="⇩This bot command detail! ⇩", color=0xffffff)
    embed.add_field(name="/help", value="This command. Command view detail.", inline=False)
    embed.add_field(name="/site_trancelate [url] [input language] [output language]", value="Typing url site is trancelate url generate. input language and output language typing ISO-638 code.", inline=False)
    embed.add_field(name="※ISO-638 code list → https://cloud.google.com/translate/docs/languages", value=" ", inline=False)
    await ctx.respond(embed=embed)

bot.run(os.environ['token'])
