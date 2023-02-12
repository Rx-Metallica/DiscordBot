import discord
import os
import json
import requests
from discord.ext import commands

bot = commands.Bot(command_prefix="!")  #using prefix command
#prefix is something that you attach before every command

bot.remove_command("help")  #removing help command


@bot.event  #events are for welcoming bots,reacton roles and lots other functions
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


"""
With async/await, you can assign the awaited function to a variable representing the returned value.
"""


#using bot.command() decorator it work on a command_prefix
@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong")


@bot.command()
async def hello(ctx):
    await ctx.channel.send("wssup")


@bot.command()
async def meme(ctx):
    meme = requests.get("https://meme-api.com/gimme")  # api for subreddit memes
    data = json.loads(meme.text) #getting data into text

    memeu = data['url']
    memename = data['title']
    memea = data['author']
    memesub = data['subreddit']
    memelink = data['postLink']

    m = discord.Embed(title=f"{memename}", color=0x3498db)  #using embeds
    m.set_image(url=memeu)
    m.set_footer(text=f"Made by: {memea} | sub by: {memesub} | post by: {memelink}")
    await ctx.send(embed=m)


@bot.command() 
async def joke(ctx): #api for Chuck Norris Jokes
    response = requests.get("https://api.chucknorris.io/jokes/random")
    data = json.loads(response.text)
    joke = data["value"]

    m = discord.Embed(title="Chuck Norris jokes", color=6435487)
    m.set_image(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fisteam.wsimg.com%2Fip%2F477dcbe8-b009-11e4-8cc0-14feb5d9f2e6%2Fols%2F39_original%2F%3A%2Frs%3Dw%3A600%2Ch%3A600&f=1&nofb=1&ipt=46dced86762d553df5f7ddfb147161214ea8e9eb305c9daa3d45314ad2aee778&ipo=images")
    m.set_footer(text=f"{joke}")
    await ctx.send(embed=m)
    #await ctx.send(joke) #returning joke


@bot.command()
async def clear(ctx, amount=100):  #clearing messages through and argument you can pass your own arguments here
    """
  Purges a list of messages that meet the criteria given by the predicate check. If a 
  check is not provided then all messages are deleted without discrimination.
  """
    await ctx.channel.purge(limit=amount)


@bot.command()
#api for Urban Dictionary 

async def dictionary(ctx, *args):  #using *args for multiple arguments
    response = requests.get(
        f"http://api.urbandictionary.com/v0/define?term={args}")
    dict = json.loads(response.text)
    dict = dict['list'][0]
    firstdef = dict["definition"]
    ups = dict['thumbs_up']
    downs = dict['thumbs_down']

    #using embeds
    m = discord.Embed(title="Urban  Dictionary", color=6451615)
    m.set_image(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fplay-lh.googleusercontent.com%2FunQjigibyJQvru9rcCOX7UCqyByuf5-h_tLpA-9fYH93uqrRAnZ0J2IummiejMMhi5Ch%3Ds180&f=1&nofb=1&ipt=b3c42c44c0a81095404b9a78a6550484fb390d4d8befb0dcfee2c4005932588d&ipo=images")
    m.set_footer(text=f"{firstdef}\nLikes: {ups} Dislikes: {downs}")
    await ctx.send(embed=m)


@bot.command()
async def help(ctx):
    #help function for commands how they work
    author = ctx.message.author
    embed = discord.Embed(title="Help Commands", color=0x7289da)
    embed.add_field(name="!ping", value="Returns Pong", inline=False)
    embed.add_field(name="!meme", value="Returns Subrredit Meme", inline=False)
    embed.add_field(name="!joke",
                    value="Returns Chuck Norris Joke",
                    inline=False)
    embed.add_field(name="!dictionary",
                    value="Returns Definition",
                    inline=False)
    embed.add_field(name="!clear", value="Clear Messages", inline=False)
    await ctx.send(author, embed=embed)


bot.run(os.getenv('TOKEN')) #bot token
