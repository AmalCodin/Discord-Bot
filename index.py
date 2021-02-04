import discord
from discord.ext import commands
import random 
import os
import discord as d
from discord.utils import get
import json
import asyncio
import os
import requests
from typing import Optional
from discord import Member, Embed
from discord.ext.commands import command, cooldown, BucketType, CommandOnCooldown
from discord.ext.commands import Cog
from datetime import datetime
from discord.ext.commands import Bot
import statcord
import emoji
import config


os.chdir("C:\\Users\\AMALSHAJI\\Documents\\Discord Bot")

client = discord.Client()
intents = discord.Intents.all()
intents.presences = True
client = commands.Bot(command_prefix="!", intents=intents)

client.remove_command('help')

key = "statcord.com-R0GKFpf0zq1PB7IlbCB9"

api = statcord.Client(client,key)

api.start_loop()


@client.event
async def on_command(ctx):
    api.command_run(ctx)


    
api_key = "2d2409cc015c720c6ffc476eb630c5f3"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

@client.command()
async def weather(ctx, *, city: str):
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel
    if x["cod"] != "404":
        async with channel.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Weather in {city_name}",
                              color=0x00ff00,
                              timestamp=ctx.message.created_at,)
            embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/kyqdHPq/Weather.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await channel.send(embed=embed)
    else:
        await channel.send("Sorry the mentioned city was not found in the database")

@client.command()
async def delrole(ctx, *,role: discord.Role):
 if ctx.author.guild_permissions.manage_roles:
   if role is None:
     await ctx.send(f'There is no such Role with the name {role} to be found in this server') 

   try:
     await role.delete()
     await ctx.send(f'The Role {role} has been deleted succesfully')

   except discord.Forbidden:
     await ctx.send('I do not have permission to delete this role')
 else:
     await ctx.send('Sorry ! You do not have the permission to use this command. Please contact Staff or Admin.')

@client.command()
async def mkrole(ctx, *, role):
    if ctx.author.guild_permissions.manage_roles:
        guild = ctx.guild
        await guild.create_role(name=role)
        await ctx.send(f"A new role {role} has been created succesfully")

@client.command()
async def leave(ctx):
    await ctx.guild.leave()
@client.command()
async def version(context):

    myEmbed = discord.Embed(title="Current Version:", description="The bot is in version 1.0", color=0x00ff00)
    myEmbed.add_field(name="Version Code:", value="Version 1.0", inline=False)
    myEmbed.add_field(name="Date Released:", value="January 1st, 2021", inline=False)
    myEmbed.set_footer(text="Hope you got to know about my version ^_^")
    myEmbed.set_author(name="Bot Made By Arcel#0001:")

    await context.message.channel.send(embed=myEmbed)



@client.command(name="help")
async def help(ctx):

    myEmbed = discord.Embed(title="All The Different Commands For The Bot:", description="**Here is the list of all the commands which are there in the Bot and can be used**", color=0x00ff00)
    myEmbed.add_field(name="User Commands:", value="**!ticket - This is one of the most useful commands used for contacting server staff regarding anything. Which can be problems you are facing in the server complains /  queries regarding the server.\n!weather City Name - This command can be used to find out the weather forecast of any city, country or place.\n !question - This command will generate a random question.\n !serverinfo - This command will show the complete Server Information.\n !whois @User - This command will give you complete information about any user in the server.\n !chmessages - Tells the total number of messages in the channel where this command is used**\n", inline=False)
    myEmbed.add_field(name="Server Staff / Admin Commands:", value="**!mute @User - This command can be used to mute any user who is breaking the rules of the server consistently.\n !unmute @User - For unmuting any use who had been muted before.\n !ban @User - This command can be used to ban any user.\n !unban @User Discord Id - To unban any user who had been banned wrongly.\n !clear (Number Of Messages) - Command for deleting messages in bulk for moderators if spamming by any user.\n !close @User - Command for closing ticket opened by any user after discussion is over.\n !mkrole Role Name - Command to make a new role quickly.\n !kick @User - To kick any user from the discord server. \n !delrole @Role - To delete any role which is not needed.\n  !slowmode Seconds - Command to set slowmode for any channel where this command is used.\n !addrole Role Name @User - Command to add any Role to any user.\n !removerole Role Name @User - Command to remove role from any user.\n !warn @User Reason - Command used to warn any user.**\n", inline=False)

    await ctx.message.channel.send(embed=myEmbed)
@client.command(name='birthday')
async def on_birthday(birthday):

        myEmbed1 = discord.Embed(title="Birthdays Channel:", description="This is a guide to show you how to add your Birthday in the birthday's channel in this server", color=0x00ff00)
        myEmbed1.add_field(name="Adding Your Birthday:", value="Type command --addbday DD/MM Format", inline=False)

        myEmbed1.add_field(name="Advantages:", value="Special Birthday Role in this server and a special announcement pinging you with a lovely birthday wish", inline=False)
        myEmbed1.set_footer(text="Hope you understood how to add your Birthday ^_^")
        myEmbed1.set_author(name="Hi Citizens,")

        await birthday.message.channel.send(embed=myEmbed1)
@client.command()
async def addrole(ctx, role: discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.manage_roles:
        await user.add_roles(role)
        await ctx.send(f"Successfully added the {role} Role to user {user}.")
    else:
        await ctx.send("Sorry ! You do not have the permission to use this command. Please contact Staff or Admin.")


@client.command()
async def removerole(ctx, role: discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.manage_roles:
        await user.remove_roles(role)
        await ctx.send(f"Successfully removed the {role} from user {user}.")
    else:
        await ctx.send("Sorry ! You do not have the permission to use this command. Please contact Staff or Admin.")

@client.event

async def when_online():

    general_channel = client.get_channel(792913689292308493)
    await general_channel.send('Hello, People')

@client.event
async def on_message(message):

    if message.content == "what is the version":
        general_channel = client.get_channel()

        myEmbed = discord.Embed(title="Current Version", description="The bot is in version 1.0", color=0x00ff00)
        myEmbed.add_field(name="Version Code:", value="Version 1.0", inline=False)
        myEmbed.add_field(name="Date Released", value="January 10th, 2021", inline=False)
        myEmbed.set_footer(text="Hope you got it")
        myEmbed.set_author(name="Made By Arcel")


        await general_channel.send(embed=myEmbed)
  
@client.event

async def on_disconnect():
    general_channel = client.get_channel(803216292282499082)
    channel2 = client.get_channel(805333221885476914)

    await channel2.message.send('I am going to be offline for sometime guys. You guys have an amazing day ahead !')
    await general_channel.message.send('I am going to be offline for sometime guys. You guys have an amazing day ahead !')

@client.command(name="kick", pass_context = True)
async def kick(context, member: discord.Member):
    if context.author.guild_permissions.kick_members:
        await member.kick()
        await context.send('User ' + member.display_name + ' has been kicked')
    else:
        await context.send("Sorry ! You do not have the permission to use this command. Please contact Staff or Admin.")
    
@client.command(name='ban', pass_context=True)
async def ban(context, member: discord.Member, *, reason=None):
    if context.author.guild_permissions.ban_members:
         await member.ban(reason=reason)
         await context.send('User ' + member.display_name + ' has been banned successfully')
    else:
        await context.send("Sorry ! You do not have the permission to use this command. Please contact Staff or Admin.")
@client.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, member:discord.Member, *, arg):
    author = ctx.author
    guild = ctx.guild
    
    channel = get(guild.text_channels, name='warn-logs')
    await ctx.send(f'{member.mention} has been warned succesfully')
    await channel.send(f'{member.mention} has been warned by {author.mention} for: {arg}')
    await member.send(f'The Moderator {author.mention} has warned you for: {arg}')

@warn.error
async def me(ctx, member:discord.Member):
    await ctx.send('You do not have the permission to use this command. Please contact Staff or Admin')


@client.command()
@commands.has_permissions(kick_members=True)
async def dawarn(ctx, member:discord.Member, *, arg):
    author = ctx.author
    guild = ctx.guild
    
    channel = get(guild.text_channels, name='🔴⌉-open-moderation')
    await ctx.send(f'{member.mention} has been warned succesfully')
    await channel.send(f'{member.mention} has been warned by {author.mention} for: {arg}')
    await member.send(f'The Moderator {author.mention} has warned you for: {arg}')

@dawarn.error
async def me(ctx, member:discord.Member):
    await ctx.send('You do not have the permission to use this command. Please contact Staff or Admin')

@client.command(name="radimg")
async def  randimg(context):
    images = ["Lmao.png", "LOL.png", "vvv.png", "vvvvvv.png", "vyttr.png"]

    random_image = random.choice(images)

    await context.send(file=discord.File(random_image))
@client.command(name = "ticket", aliases=["support"])
@commands.has_permissions()
@cooldown(1, 25, BucketType.guild)
async def ticket(ctx):
    author = ctx.author
    guild = ctx.guild
    channel = get(guild.text_channels, name='Support')
    available_staff = get(ctx.guild.roles, name="Staff Team")
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True),
        author: discord.PermissionOverwrite(read_messages=True),
        available_staff: discord.PermissionOverwrite(read_messages=True)
    }
    
    channel = await guild.create_text_channel('support-channel', overwrites=overwrites)
    await channel.send(f'Hi! {author.mention} I have created a support channel for you. You can write your queries/complain here and one of the staff from the {available_staff.mention} will be immediately replying to your queries/complain very soon')
@ticket.error
async def on_command_error(ctx, exc):
    if on_command_error(exc, CommandOnCooldown):
        await ctx.send("You already have a support channel open. Kindly wait for your current support channel to be closed by a Staff. Thanks ^_^")

@client.command()
async def close(ctx, member: discord.Member): 
    channel = discord.utils.get(ctx.guild.channels, name='support-channel')
    nbed = d.Embed(
        title = 'Success',
        description = 'Support Channel:  has been closed !',
    )
    if ctx.author.guild_permissions.manage_channels:
        await ctx.send(embed=nbed)
        await channel.delete()
        await member.send(f'Hi! {member.mention} Your support channel has been closed by one of the Staff to open a new support channel please do !ticket again')


@client.command(pass_context=True)
async def question(ctx):
    questions = ["Are you a morning person or a night owl ?","Do you prefer mental or physical exercise ?","What achievement are you most proud of ?","What annoys you ?","What country or place in the world would you most/least like to visit ?","Do you follow your horoscope ?",]
    await ctx.send(format(random.choice(questions)))

filtered_words = ["Faggot","nigger","faggot", "Transvestite","twat","boob"," anal","bloody bitch", "asshole", "son of a bitch"]

@client.event
async def on_message(msg):
    context = msg.channel
    author = msg.author
    myEmbed2 = discord.Embed(title="Your Message Was Flagged Inappropriate:", description=f'{author.mention} your message had some words which is not to be used in this server we kindly request you to refrain from using such words in this server', color=0x00ff00)
    myEmbed2.add_field(name="Thank You", value="  -----------------------------------------------------------  ")
    myEmbed2.set_footer(text="Enjoy your stay in this server and have a great day ahead ^_^")
    myEmbed2.set_author(name=f'Hi {author},')

    for word in filtered_words:
        if word in msg.content:
            await context.send(embed=myEmbed2)

    await client.process_commands(msg)



@client.command(name="whois", aliases=["userinfo", "ui"])
async def userinfo(ctx, target: Member):
    target = target or ctx.author
    embed = Embed(title="User Information:",
    color = 0x00ff00,
    timestamp=datetime.utcnow())
    embed.set_thumbnail(url=target.avatar_url)
    fields = [("Discord Usermame:", str(target), True),
    ("Discord ID:", target.id, True),
    ("Is User A Bot ?", target.bot, True),
    ("User Top Role:", target.top_role.mention, True),
    ("Current Status:", str(target.status).title(), True),
    ("Current Activity:", f"{str(target.activity.type).split('.')[-1].title() if target.activity else 'Not Known'} {target.activity.name if target.activity else ''}", True),
    ("Account Created In Discord:", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
    ("Joined Server At:", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True),
    ("Did User Boosted This Server:", bool(target.premium_since), True)]
    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)
    await ctx.send(embed=embed)
                      
@client.command()
async def serverinfo(ctx):
    embed = Embed(title="Server Information:", 
    color = 0x00ff00,
                  timestamp = datetime.utcnow())

    embed.set_thumbnail(url=ctx.guild.icon_url)


    statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]


    fields = [("Server ID:", ctx.guild.id, True),
              ("Owner:", str(ctx.guild.owner), True),
              ("Region:", ctx.guild.region, True),
              ("Created At:", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
              ("Member Count:", ctx.guild.member_count, True),
              ("No. Of Human Members:", len([m for m in ctx.guild.members if not m.bot]), True),
              ("No. Of Bots:", len([m for m in ctx.guild.members if m.bot]), True),
              ("No. Of Banned Members:", len(await ctx.guild.bans()), True),
              ("Member Statuses:", f"🟢 {statuses[0]} 🟠 {statuses[1]} 🔴 {statuses[2]}", True),
              ("No. Text Channels:", len(ctx.guild.text_channels), True),
              ("No. Of Voice Channels:", len(ctx.guild.voice_channels), True),
              ("No. Of Categories:", len(ctx.guild.categories), True),
              ("No. Of Roles:", len(ctx.guild.roles), True),
              ("No. Of Invites:", len(await ctx.guild.invites()), True),
              ("\u200b", "\u200b", True)]
    for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)
    await ctx.send(embed=embed)
    

@client.command(name="serverinformation", aliases=["guildinfo", "si", "gi"])
async def server_info(self, ctx):
    pass

@client.command()
async def chmessages(ctx, channel: discord.TextChannel=None):
    channel = channel or ctx.channel
    count = 0
    async for _ in channel.history(limit=None):
        count += 1
    await ctx.send("There are {} messages in {}".format(count, channel.mention))
    

@client.event
async def on_ready():
    return await client.change_presence(status=discord.Status.online, activity=discord.Game('How to be a bot'))

watch = [{"name":"Watch","price":500,"description":"To Work As A Watch Repair Person"}]
laptop = [{"name":"Laptop","price":1000,"description":"Work Remotely"}]

mainshop = [
{"name":"PS-5","price":10000,"description":"Gaming Console With Games To Play With Other Server Members"}]

gun = [{"name":"Rifle","price": 20000,"description":"Those who have this Rifle can use the !shoot command while working as an Army General this will give more money compared to other Army jobs"}]
limited = [{"name":"Arcelean-Trophy","price": 100000,"description":"One of the best items you can have in the entire shop those who have this item are represented as the top honary people"}]
coin = [
{"name":"Supa-Coin","price":50000,"description":"The rarest unique coin obtainable. Users having this coin in their bag are truly special and have been very rich."}]

killer = [{"name": "Sword","price": 5000,"description":"Those who have this Sword can use the !stab command while working as an Army General this will give more money compared to other Army jobs"}]

dog = [{"name":"Puppy","price":6000,"description":"For those who wants to have a cute Puppy as their pet or likes Puppies/Dogs"}]

cat = [{"name":"Kitten","price":6000,"description":"For those who wants to have a cute Kitten as their pet or likes Kittens/Cats"}]

dragon = [{"name":"Dragon","price":50000,"description":"The most expensive pet that is available. Why expensive ? Because it is the best pet you can own in the entire game only the Rich can afford this pet"}]
@client.command(name = "petshop")
async def petshop(ctx):
    em = discord.Embed(title = "Pet Shop", color = 0x00ff00)
    em.set_thumbnail(url='https://media1.tenor.com/images/872da3ec5bb0565e58608ac693222bf8/tenor.gif?itemid=12851514')
    
    em2 = discord.Embed(title = '', color = 0x00ff00)
    
    em2.set_thumbnail(url='https://media1.tenor.com/images/8ab88b79885ab587f84cbdfbc3b87835/tenor.gif?itemid=15917800')

    em3 = discord.Embed(title = '', color = 0x00ff00)
    
    em3.set_thumbnail(url='https://media.giphy.com/media/5SsG3AVUUpLOM/giphy.gif')


    for item in dog:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name = name, value = f"${price} | {desc}")
    
    for item in cat:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em2.add_field(name = name, value = f"${price} | {desc}")

    for item in dragon:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em3.add_field(name = name, value = f"${price} | {desc}")


    await ctx.send(embed = em)
    await ctx.send(embed = em2)
    await ctx.send(embed = em3)

    
@client.command()
async def shop2(ctx):
    em = discord.Embed(title = 'Collectible Limited Items:', color = 0x00ff00)
    em.set_thumbnail(url='https://media.tenor.com/images/d20fe4685cf0b6b8acff74ef9954e5ea/tenor.gif')

    em2 = discord.Embed(title = '', color = 0x00FFFF)
    em2.set_thumbnail(url='https://cdn.dribbble.com/users/1396216/screenshots/7009112/600x800.gif')

    for item in limited:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name = name, value = f"${price} | {desc}")
    
    for item in coin:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em2.add_field(name = name, value = f"${price} | {desc}")

    await ctx.send(embed = em)
    await ctx.send(embed = em2)
@client.command()
async def shop(ctx):
    em4 = discord.Embed(title = "Shop:", description = "**To Purchase Items For Working Or Having Fun !**", color = 0x00ff04)
    em = discord.Embed(title = " ", color = 0x00ff00)
    em.set_thumbnail(url='https://media1.giphy.com/media/V6Y9IpDepemUB9IWbd/giphy.gif')

    em2 = discord.Embed(title = "", color = 0x00ff00)
    em2.set_thumbnail(url='https://media2.giphy.com/media/IJamPSQFcUyHK/giphy.gif')

    em3 = discord.Embed(title = " ", color = 0x00ff00)
    em3.set_thumbnail(url='https://media3.giphy.com/media/UcK7JalnjCz0k/giphy.gif')

    em5 = discord.Embed(title = "", color = 0x00ff00)
    em5.set_thumbnail(url='https://media.giphy.com/media/Y1vGeYTB8Kpqw/giphy.gif')

    em6 = discord.Embed(title = "", color = 0x00ff00)
    em6.set_thumbnail(url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/b3e7fc81-b38f-424e-b6e6-c895a3f441d9/dbfasp8-9e60f055-06cf-4601-9473-675ea61e58e0.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvYjNlN2ZjODEtYjM4Zi00MjRlLWI2ZTYtYzg5NWEzZjQ0MWQ5XC9kYmZhc3A4LTllNjBmMDU1LTA2Y2YtNDYwMS05NDczLTY3NWVhNjFlNThlMC5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.fg0MTVPns_A6QrwfyrgYfDb7ZfyCOdIayUZMYjBAd-4")
      
    
    for item in killer:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em6.add_field(name = name, value = f"**$ {price} | {desc}**")
        

    for item in gun:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em5.add_field(name = name, value = f"**$ {price} | {desc}**")
        


    for item in watch:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em2.add_field(name = name, value = f"**$ {price} | {desc}**")
        



    for item in laptop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em3.add_field(name = name, value = f"**$ {price} | {desc}**")

    


    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name = name, value = f"**$ {price} | {desc}**")


    await ctx.send(embed = em4)   


    await ctx.send(embed = em2)

    await ctx.send(embed = em3)

    await ctx.send(embed = em)

    await ctx.send(embed = em5)

    await ctx.send(embed = em6)






@client.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("The item you mentioned is not available in the shop right now")
            return
        if res[1]==2:
            await ctx.send(f"You do not have enough money in your wallet to buy {item}")
            return

    await ctx.send(f"Contragulations ! You just bought {amount} {item} the item has been added to your bag")

@client.command()
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []

    em = discord.Embed(title = f"{ctx.author.name}'s Bag", color = 0x00ff00)
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value= amount)
        em.set_thumbnail(url='https://media.giphy.com/media/McIZk48IDPC5Ndg27p/giphy.gif')


    await ctx.send(embed = em)
library1 = [{"name":"Cool-Book","price": 0,"description":"This book is so cool"}]
async def get_library(user,item_name,amount):

    item_name = item_name.lower()
    name_ = None
    for item in library1:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            
 
            break


    if name_ == None:
        pass

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

 

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1
        if t == None:
            obj = {"item":item_name, "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name, "amount" : amount}
        users[str(user.id)]["bag"] = [obj]

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]



async def buy_this(user,item_name,amount):

    item_name = item_name.lower()
    name_ = None
    for item in limited:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            
    for item in gun:
        
        name = item["name"].lower()
        
        if name == item_name:
            name_ = name
            price = item["price"]
            
    for item in killer:
        
        name = item["name"].lower()
                
        if name == item_name:
            
            name_ = name
            
            price = item["price"]
                    
    for item in coin:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]


    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]


    for item in watch:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]

    for item in laptop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]

    for item in cat:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]

    for item in dragon:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]


    for item in dog:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break


    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1
        if t == None:
            obj = {"item":item_name, "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name, "amount" : amount}
        users[str(user.id)]["bag"] = [obj]

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]

@client.command(name = "lb", aliases = ["rich", "richest"])
async def lb(ctx, x = 5):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)

    em = discord.Embed(title = f"Top {x} Richest People:", description = "This is the list of the **Top 5 Richest People** in the game decided on the basis of the amount of money they have in both their wallet and bank.", color = 0x00ff00)

    em.set_thumbnail(url='https://media2.giphy.com/media/hvFUiCVOECDXJueNdy/giphy.gif?cid=ecf05e47a8ahlvcd47ozm07u3jdulh18salsxed12a4l3klg&rid=giphy.gif')
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        mem = client.get_user(id_)
        name = mem.name
        em.add_field(name = f"{index}. {name}", value=f"{amt}", inline = False)

        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)


@client.command(name="bal", aliases = ["balance", "b"])
async def bal(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()
    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title=f"{ctx.author.name}'s Balance:", color=0x00ff00)
    em.set_thumbnail(url='https://media0.giphy.com/media/mgByAN6FfHTnq/giphy.gif?cid=ecf05e47gt9k664gqxune4b1ut7blpvjl5npjxc93fs17wq1&rid=giphy.gif')
    em.add_field(name = "Wallet Balance:", value = wallet_amt)
    em.add_field(name = "Bank Balance:", value = bank_amt)
    await ctx.send(embed = em)


async def get_bank_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)
    return users


async def update_bank(user, change = 0, mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json", "w") as f:
        json.dump(users,f)

    bal = users[str(user.id)]["wallet"],users[str(user.id)]["bank"]
    
    return bal


async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
    with open("mainbank.json", "w") as f:
        json.dump(users,f)
    return True

@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()
    
    users[str(user.id)]["wallet"]

    earnings = random.randrange(101)

    await ctx.send(f"Someone gave you {earnings} coins")

    users[str(user.id)]["wallet"] += earnings
    with open("mainbank.json", "w") as f:
        json.dump(users,f)

@beg.error
async def beg_error(ctx,error):
    
    if isinstance(error, commands.CommandOnCooldown):

        em = discord.Embed(color = 0x00FFFF)
        em.add_field(name = "Wait Sometime..", value = f'This command is on cooldown, you can **Beg Again** after **{round(error.retry_after)} Seconds**')
        
        await ctx.send(embed = em)


@client.command(name="withdraw", aliases = ["with", "w"])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount you want to withdraw from your Bank")
        return

    bal = await update_bank(ctx.author)


    amount = int(amount)

    if amount>bal[1]:
        await ctx.send("Sorry ! You do not have that much money in your Bank to withdraw")
        return
    if amount<0:
        await ctx.send("Amount must be Positive !")
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,"bank")

    await ctx.send(f"You withdrew **$ {amount}** from your Bank")


        # The `amount` variable is now a positive integer, deposit it here

@client.command()
async def dep(ctx,amount = None):
    await open_account(ctx.author)



    if amount == None or amount == "max" or amount == "all":
        await ctx.send("Please enter the amount you want to deposit in **Digits (1, 10, 100 etc)**")
        return

    bal = await update_bank(ctx.author)


    amount = int(amount)

    if amount>bal[0]:
        await ctx.send("Sorry ! You do not have that much money to deposit")
        return
    if amount<0:
        await ctx.send("Amount must be Positive !")

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,"bank")

    await ctx.send(f"You deposited **$ {amount}** into your Bank ")


@client.command()
async def trade(ctx,member: discord.Member,item):
    await open_account(ctx.author)
    await open_account(member)
    if item == None:
        await ctx.send("Please enter the name of the item in your bag that you want to use for the trade")
        return
    bag = await update_bank(ctx.author)

    item = int(item)

    if item == "watch":
        update_bank(ctx.author,-1*watch)
        
        await update_bank(ctx.author,-1*item,"watch")
        await update_bank(member,item,"watch")

        await ctx.send(f"{ctx.author.mention} You gave {item} to the user {member.Name}")

@client.command()
async def give(ctx,member: discord.Member,amount = None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)


    amount = int(amount)

    if amount>bal[1]:
        await ctx.send("Sorry ! You do not have that much money in your bank to give someone")
        return
    if amount<0:
        await ctx.send("Amount must be Positive !")

    await update_bank(ctx.author,-1*amount,"bank")
    await update_bank(member,amount,"bank")

    await ctx.send(f"You gave **$ {amount}** to {member}")

@client.command()
async def bet(ctx,amount = None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Please enter the amount you want to place a bet in **Digits (1, 10, 100 etc)**")
        return

    bal = await update_bank(ctx.author)


    amount = int(amount)
    if amount>bal[0]:
        await ctx.send(f"You do not have that much money in your wallet to place a bet of ** $ {amount}**")
        return
    if amount == 0:
        await ctx.send("Please enter an amount of money you want to place a bet that is any digit other than zero")
        return
    if amount<0:
        await ctx.send("Amount must be positive !")
        return

   
        
    final = []

    for a in range(3):
        a = emoji.emojize(random.choice([":o:",":x:",":red_circle:"]))

        final.append(a)

    await ctx.send(str(final))


    if final[0] == final[1] or final[2] == final[1]:
        await update_bank(ctx.author,0.5*amount)
        await ctx.send(f"Contragulations ! You won $ {1/2*amount}")
    
    else:
        await update_bank(ctx.author,-1*amount)

        await ctx.send(f"You lost $ {amount}")







@client.command()
async def rob(ctx,member: discord.Member,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    amount = int(amount)
    bal = await update_bank(member)


    if bal[0]<100:
        await ctx.send("It's not worth it !")
        return

    earnings = random.randrange(0, bal[0])


    await update_bank(ctx.author,earnings)
    await update_bank(ctx.author,-1*earnings)

    await ctx.send(f"You robbed and got {amount} coins !")

@client.command()
async def work(ctx):
    
    em = discord.Embed(title = "Different Types Of Jobs Available:", color = 0xfff00)

    em.add_field(name = "Watch Repair Person:", value = "To work as a Watch Repair Person you **must purchase a watch from the shop**. The command to work as a Watch Repair Person is **!work1**", inline = False)

    em.add_field(name = "Programmer:", value = "To work as a Programmer you **must purchase a laptop from the shop**. The command to work as a Programmer is **!work2**", inline = False)

    await ctx.message.channel.send(embed=em)


@client.command()
@commands.cooldown(1, 300, commands.BucketType.user)
async def work2(ctx):

    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()


    for item in users[str(user.id)]["bag"]:
        if item["item"] == "laptop":
            user = ctx.author
            users[str(user.id)]["wallet"]
            earnings = random.randint(390, 500)
            programming_languages = ["Java", "C ++", "Python", "Cotlin", "Javascript", "GO", "Cotlin", "Ruby", "Swift", "C"]
            gif = ["https://media2.giphy.com/media/349qKnoIBHK1i/giphy.gif?cid=ecf05e47de1819407cf1d9581987ca63da0c1c62ef9c3a3c&rid=giphy.gif", "https://media1.giphy.com/media/ZVik7pBtu9dNS/giphy.gif", "https://media0.giphy.com/media/LmNwrBhejkK9EFP504/giphy.gif?cid=ecf05e47650064b0600d74c7f00a72aa76511ba84f533846&rid=giphy.gif", "https://media2.giphy.com/media/13HgwGsXF0aiGY/giphy.gif?cid=ecf05e473c541d86e34e9712e0f4fdd64c7e25d7b53e9e68&rid=giphy.gif", "https://media3.giphy.com/media/MGdfeiKtEiEPS/giphy.gif?cid=ecf05e471f4d3bcbde04028e40a71b45b5d3b8bf5871beca&rid=giphy.gif"]
            em = discord.Embed(title = f"You worked as a **{random.choice(programming_languages)} Programmer** and earned **$ {earnings}**", color = 0x00FFFF)
            em.set_image(url = random.choice(gif))
            
            await ctx.send(embed = em)
    
            users[str(user.id)]["wallet"] += earnings
            
            with open("mainbank.json", "w") as f:
                json.dump(users,f)
                break


@work2.error
async def work2_error(ctx,error):
    
    if isinstance(error, commands.CommandOnCooldown):

        em = discord.Embed(color = 0x00FFFF)
        em.add_field(name = "Wait Sometime..", value = f'This command is on cooldown, you can **Work Again** after **{round(error.retry_after)} Seconds**')
        
        await ctx.send(embed = em)





@client.command()
@commands.cooldown(1, 60000, commands.BucketType.user)

async def daily(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    author = ctx.author

    earnings = random.randint(3000, 4000)

    em = discord.Embed(title = "Here Is Your Daily Reward:", value = f"You have received **$ {earnings}** the money has been added to your wallet succesfully" )
    em.set_author(name = f"Hi {author.name},")
    em.add_field(name = "-------------------------------------", value=f"You have received **$ {earnings}** the money has been added to your wallet succesfully")

    await ctx.send(embed = em)

    users[str(user.id)]["wallet"] += earnings
    
    with open("mainbank.json", "w") as f:
        
        json.dump(users,f)
                

@daily.error
async def daily_error1(ctx,error):
    
    if isinstance(error, commands.CommandOnCooldown):

        em = discord.Embed(color = 0x00FFFF)
        em.add_field(name = "You Already Claimed..", value = f'You have already claimed your Daily Reward for today come back again tommorow to claim your Daily Reward')
        
        await ctx.send(embed = em)


@client.command()
@commands.cooldown(1, 100, commands.BucketType.user)
async def work1(ctx):

    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    for item in users[str(user.id)]["bag"]:
        if item["item"] == "watch" or "laptop":
            user = ctx.author
            users[str(user.id)]["wallet"]
            earnings = random.randint(100, 200)
            gif = ["https://media1.giphy.com/media/3o72FhGxehNdI4Ukc8/giphy.gif?cid=ecf05e47hs538h67ng3v96c212a3zag93afg4q63pxwkg3dd&rid=giphy.gif", "https://thumbs.gfycat.com/ReadySoulfulAntlion-size_restricted.gif", "https://media2.giphy.com/media/ME96jemLMJA7x4cZyu/giphy.gif?cid=ecf05e47628ce413f0c17ff7e262a33ac33b70b2ac2b6894&rid=giphy.gif", "https://media.giphy.com/media/3o6ZthFR9AtTyAylz2/giphy.gif"]
            em = discord.Embed(title = f"You worked as a **Watch Repair Person** and earned **$ {earnings}**", color = 0x00FFFF)
            em.set_image(url = random.choice(gif))
            
            await ctx.send(embed = em)

    
            users[str(user.id)]["wallet"] += earnings
            
            with open("mainbank.json", "w") as f:
                json.dump(users,f)
                break
        if item["item"] != "watch":
            await ctx.send("You need to **Purchase A Watch** from the shop in order to unlock this job. Do !shop to checkout the shop.")
@client.command()
@commands.cooldown(1, 1800, commands.BucketType.user)
async def special(ctx):

    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()
    
    users[str(user.id)]["wallet"]
    
    earnings = random.randint(1000, 1400)
    
    em = discord.Embed(color = 0x00FFFF)
    em.add_field(name = "Superb Army General !", value = f"**You Defeated The Enemy Using Your Special Attack \n As you did the job very well you are Rewarded with $ {earnings}\n Hope to see you at the battlefield again very soon until then take care General !**")
   
    await ctx.send(embed = em)
    
    users[str(user.id)]["wallet"] += earnings
    
    with open("mainbank.json", "w") as f:
        json.dump(users,f)

@client.command()
@commands.cooldown(4, 1800, commands.BucketType.user)
async def work3(ctx):

     em = discord.Embed(color = 0x00FFFF)
     
     em.add_field(name="Are Ready To Take Up The Big Challenge ?", value = "Would you like to work as an Army Officer if yes do **!yes**  to continue")
     
     em.set_thumbnail(url="https://media.giphy.com/media/eTH6uICbjrc9G/giphy.gif")
     
     await ctx.send(embed = em)
@work3.error
async def work_error3(ctx,error):
    
    if isinstance(error, commands.CommandOnCooldown):

        em = discord.Embed(color = 0x00FFFF)
        em.add_field(name = "Hey Army General..", value = f'This command is on cooldown, you can **Battle Again** after **{round(error.retry_after)//60} Minutues**')
        
        await ctx.send(embed = em)
@client.command()
@commands.cooldown(1, 1800, commands.BucketType.user)
async def stamp(ctx):
    em = discord.Embed(color = 0x00FFFF)
    em.add_field(name = "You Stamped The Enemy !", value = "Now they are stamping you back do **!block** to block yourself from their hit")

    await ctx.send(embed = em)
@stamp.error
async def stamp_error(ctx,error):
    
    if isinstance(error, commands.CommandOnCooldown):

        em = discord.Embed(color = 0x00FFFF)
        em.add_field(name = "Hey Army General..", value = f'This command is on cooldown, you can **Battle Again** after **{round(error.retry_after)//60} Minutues**')
        
        await ctx.send(embed = em)
@client.command()
@commands.cooldown(1, 1800, commands.BucketType.user)
async def block(ctx):
    
    em = discord.Embed(color = 0x00FFFF)
    em.add_field(name = "You Dodged The Enemies Stamp !", value = "Now its time to finish off this enemy is'nt it ? Do **!special** to use your special attack on the enemy such that they Die")


    await ctx.send(embed = em)
@block.error
async def block_error(ctx,error):
    
    if isinstance(error, commands.CommandOnCooldown):

        em = discord.Embed(color = 0x00FFFF)
        em.add_field(name = "Hey Army General..", value = f'This command is on cooldown, you can **Battle Again** after **{round(error.retry_after)//60} Minutues**')
        
        await ctx.send(embed = em)
@client.command()
@commands.cooldown(4, 1800, commands.BucketType.user)
async def yes(ctx):
           em = discord.Embed(color = 0x00FFFF)
           
           em.add_field(name="Welcome To The Club This Is Not Going To Be An Easy One", value="You are now an Army general fighting for your country", inline=False)
           em.add_field(name="\nArmy Officer Commands:", value="**!shoot**- To shoot the enemy. Must purchase a Rifle from the shop to use this command. \n **!punch** - To punch the enemy \n **!stamp** - To stamp the enenmy \n **!stab** - To stab the enemy. Must purchase a knife from the shop", inline=False)
           
           em.add_field(name="\nHow to earn more as an Army Officer ?", value="The more better attacks you do that is if you **shoot, stab** an enemy you get more money compared to kick and punch commands", inline=False)
           
           em.add_field(name="\nSo what are you waiting for ?", value="Go fight them !", inline=False)
           
           await ctx.send(embed = em)
@yes.error
async def yes_error(ctx,error):
    
    if isinstance(error, commands.CommandOnCooldown):

        em = discord.Embed(color = 0x00FFFF)
        em.add_field(name = "Hey Army General..", value = f'This command is on cooldown, you can **Battle Again** after **{round(error.retry_after)//60} Minutues**')
        
        await ctx.send(embed = em)

@client.command()
@commands.cooldown(1, 1800, commands.BucketType.user)
async def punch(ctx):
    
    em = discord.Embed(color = 0x00FFFF)
    em.add_field(name = "You Punched The Enemy !", value = "Now they are punching you back do **!defend** to block yourself from their hit")

    await ctx.send(embed = em)
    
@punch.error
async def punch_error(ctx,error):
    
    if isinstance(error, commands.CommandOnCooldown):

        em = discord.Embed(color = 0x00FFFF)
        em.add_field(name = "Hey Army General..", value = f'This command is on cooldown, you can **Battle Again** after **{round(error.retry_after)//60} Minutues**')
        
        await ctx.send(embed = em)
    

@client.command()
@commands.cooldown(1, 1800, commands.BucketType.user)
async def defend(ctx):
    
    em = discord.Embed(color = 0x00FFFF)
    em.add_field(name = "You Defended The Enemies Hit !", value = "Now its time to finish off this enemy is'nt it ? Do **!hitback** to give a strong hit to the enemy such that they Die this hit they will remember forever")


    await ctx.send(embed = em)

@defend.error
async def defend_error(ctx,error):
    
    if isinstance(error, commands.CommandOnCooldown):

        em = discord.Embed(color = 0x00FFFF)
        em.add_field(name = "Hey Army General..", value = f'This command is on cooldown, you can **Battle Again** after **{round(error.retry_after)//60} Minutues**')
        
        await ctx.send(embed = em)
@client.command()
@commands.cooldown(1, 1800, commands.BucketType.user)
async def hitback(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()
    
    users[str(user.id)]["wallet"]
    
    earnings = random.randint(1000, 1400)
    
    em = discord.Embed(color = 0x00FFFF)
    em.add_field(name = "Bravo Army General !", value = f"**You Defeated The Enemy \n As you did the job very well you are Rewarded with $ {earnings}.\n Hope to see you at the battlefield again very soon until then take care General !**")
   
    await ctx.send(embed = em)
    
    users[str(user.id)]["wallet"] += earnings
    
    with open("mainbank.json", "w") as f:
        json.dump(users,f)

@hitback.error
async def hit_backerror(ctx,error):
    if isinstance(error, commands.CommandOnCooldown):
        
        user = ctx.author
        
        users = await get_bank_data()
        
        users[str(user.id)]["wallet"]     

        earnings = 800

        em = discord.Embed(color = 0x00FFFF)
        em.add_field(name = "You Think You Are Smart ?", value = f'You have been fined **$ 800** for trying to use only the **!hitback** command the money has been deducted from your balance', inline=False)
        em.add_field(name = "How To Avoid This From Happening ?", value = "Never use the **!hitback** command alone", inline=False)
        await ctx.send(embed = em)
    users[str(user.id)]["wallet"] -= earnings
    
    with open("mainbank.json", "w") as f:
        json.dump(users,f)

       
@work1.error
async def work_error1(ctx,error):
    
    if isinstance(error, commands.CommandOnCooldown):

        em = discord.Embed(color = 0x00FFFF)
        em.add_field(name = "Wait Sometime..", value = f'This command is on cooldown, you can **Work Again** after **{round(error.retry_after)} Seconds**')
        
        await ctx.send(embed = em)

@client.command()
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)


    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1]==3:
            await ctx.send(f"You don't have {item} in your bag.")
            return

    await ctx.send(f"Successfully Sold {amount} {item} the money has been added to your balance")

async def sell_this(user,item_name,amount,price = None):

    item_name = item_name.lower()
    name_ = None

    for item in gun:
        
        name = item["name"].lower()
        
        if name == item_name:
            
            name_ = name
            
            if price==None:
                
                price = 0.9* item["price"]
    for item in killer:
        
        name = item["name"].lower()
        
        if name == item_name:
            
            name_ = name
            
            if price==None:
                
                price = 0.9* item["price"]

    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.9* item["price"]
    for item in watch:
        
        name = item["name"].lower()
        
        if name == item_name:
            
            name_ = name
            
            if price==None:
                
                price = 0.9* item["price"]

    for item in laptop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.9* item["price"]




    
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]


@client.command()
@commands.cooldown(1, 3000, commands.BucketType.user)
async def stab(ctx):

    army_replies = ["**Good Work !** You stabbed the enemy and they died", "**Very Good !**  You stabbed the enemy down and they died", "Oh No ! The enemy stabbed you before you stabbed them and you died RIP", "**Amazing !**  You stabbed the enemy and they died"]

    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    earnings = random.randint(1000, 1500)


    for item in users[str(user.id)]["bag"]:

        if item["item"] == "sword":
            if random.choice(army_replies) == str("Oh No ! The enemy stabbed you before you stabbed them and you died RIP"):
                
                await ctx.send("Oh No ! The enemy stabbed you before you stabbed them and you died RIP")
                
                return
            if random.choice(army_replies) != "Oh No ! The enemy stabbed you before you stabbed them and you died RIP":
                
                user = ctx.author
                
                users[str(user.id)]["wallet"]
                
                await ctx.send(f"{random.choice(army_replies)} for doing your work you earned **$ {earnings}**")
                
                users[str(user.id)]["wallet"] += earnings
                
                with open("mainbank.json", "w") as f:
                    
                    json.dump(users,f)
                    
                    break



@stab.error
async def moot_error3(ctx,error):
    
    if isinstance(error, commands.CommandOnCooldown):

        em = discord.Embed(color = 0x00FFFF)
        em.add_field(name = "Hey Army General..", value = f'This command is on cooldown, you can **Stab Enemy Again** after **{round(error.retry_after)//60} Minutues**')
        
        await ctx.send(embed = em)

@client.command()
@commands.cooldown(1, 3000, commands.BucketType.user)
async def walk(ctx):
    
    army_replies = ["**So Sweet !** You took your little Puppy for a walk in the Park", "**Nice !**  You took your puppy for a walk in the Garden", "Your puppy is so happy and is Barking softly at you because you took it out for a walk", "Your puppy is so happy it has such a caring master who takes it for walk"]

    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    earnings = random.randint(100, 200)


    for item in users[str(user.id)]["bag"]:

        if item["item"] == "puppy":

                user = ctx.author
                
                users[str(user.id)]["wallet"]
                
                await ctx.send(f"{random.choice(army_replies)} it costed you **$ {earnings}**")
                
                users[str(user.id)]["wallet"] -= earnings
                
                with open("mainbank.json", "w") as f:
                    
                    json.dump(users,f)
                    
                    break
        
@client.command()
@commands.cooldown(1, 3000, commands.BucketType.user)
async def shoot(ctx):

    army_replies = ["**Good Work !** You shot the enemy down and they died", "**Very Good !**  You shot the enemy down and they died", "Oh No ! The enemy shot you before you shot them and you died RIP", "**Amazing !**  You shot the enemy down and they died"]

    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    earnings = random.randint(2000, 3000)


    for item in users[str(user.id)]["bag"]:

        if item["item"] == "rifle":
            if random.choice(army_replies) == str("Oh No ! The enemy shot you before you shot them and you died RIP"):
                
                await ctx.send("Oh No ! The enemy shot you before you shot them and you died RIP")
                
                return
            if random.choice(army_replies) != "Oh No ! The enemy shot you before you shot them and you died RIP":
                
                user = ctx.author
                
                users[str(user.id)]["wallet"]
                
                await ctx.send(f"{random.choice(army_replies)} for doing your work you earned **$ {earnings}**")
                
                users[str(user.id)]["wallet"] += earnings
                
                with open("mainbank.json", "w") as f:
                    
                    json.dump(users,f)
                    
                    break
@shoot.error
async def shoot_error3(ctx,error):
    
    if isinstance(error, commands.CommandOnCooldown):

        em = discord.Embed(color = 0x00FFFF)
        em.add_field(name = "Hey Army General..", value = f'This command is on cooldown, you can **Shoot Again** after **{round(error.retry_after)//60} Minutues**')
        
        await ctx.send(embed = em)
@client.command()
@commands.has_permissions(manage_messages=True, manage_channels=True)
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount)
@client.command(name='contact')
async def birthday(birthday):

        myEmbed2 = discord.Embed(title="Staff Team:", description="Want to contact the Staff Team for anything regarding the server ? You have come to the right place read on", color=0x00ff00)
        myEmbed2.add_field(name="Staff Team:", value="Prisuma Zexicon: Server Owner", inline=False)
        myEmbed2.add_field(name="--------------------------------------", value="Pyro: Co-Owner", inline=False) 
        myEmbed2.add_field(name="--------------------------------------", value="Hannah, Pinneapple: The Council", inline=False) 
        myEmbed2.add_field(name="--------------------------------------", value="Arcel: Staff Manager", inline=False)
        myEmbed2.add_field(name="Way To Contact:", value="If you have any query just ping any of them in any channel they will respond as soon as they can to your query", inline=False)
        myEmbed2.set_footer(text="Hope you understood how to contact the staff of this server ^_^")
        myEmbed2.set_author(name="Hi Citizens,")

        await birthday.message.channel.send(embed=myEmbed2)
@client.command(aliases=['ub'])
@commands.has_permissions(ban_members = True)
async def unban(ctx, *,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member_name,member_disc):

            await ctx.guild.unban(user)
            await ctx.send("User " + member_name + " has been unbanned")
            return
        else:
            await ctx.send("Sorry ! You do not have the permission to use this command. Please contact Staff or Admin.")

@client.command()
async def search(ctx):

    em = discord.Embed(title = "Searchable Location Commands:", color = 0xFFD700)
    em.add_field(name = "**!garden:**", value="To search the Garden", inline = False)
    em.add_field(name = "**!pocket:**", value="To search your Pocket", inline = False)
    em.add_field(name = "**!pantry:**", value="To search the Pantry", inline=False)
    em.add_field(name = "**!library:**", value="To search the Library", inline = False)
    
    await ctx.send(embed = em)
@client.command()
async def library(ctx, item=str("Cool-Book"), amount=1):
    await open_account(ctx.author)

    res = await get_library(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("The item you mentioned is not available in the shop right now")
            return
        if res[1]==2:
            await ctx.send(f"You do not have enough money in your wallet to buy {item}")
            return

    await ctx.send(f"Contragulations ! You searched the library and found {amount} {item} the book has been added to your bag")

  
        
                   


    
@client.command(name = "pantry")
@commands.cooldown(1, 240, commands.BucketType.user)
async def pantry(ctx):

    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()
    earnings = random.randint(200, 250)
    earnings2 = 0
    reply1 = [f"**Cool !** You searched the Pantry and found **$ {earnings}**", f"**Superb !** You searched the Pantry and found **$ {earnings}**", f"**Wow !** You searched the Pantry and found **$ {earnings}**", f"**Lovely !** You searched the Pantry and found **$ {earnings}**", f"**Your Lucky !** You searched the Pantry and found **$ {earnings}**"]
    
    users[str(user.id)]["wallet"] += earnings
    
    with open("mainbank.json", "w") as f:
        
        json.dump(users,f)
    


    await ctx.send(random.choice(reply1))

@client.command()
@commands.cooldown(1, 240, commands.BucketType.user)
async def garden(ctx):
    
    await open_account(ctx.author)

    user = ctx.author
    users = await get_bank_data()
    earnings = random.randint(100, 200)

    reply1 = [f"**Cool !** You searched the Garden and found **$ {earnings}**", f"**Superb !** You searched the Garden and found **$ {earnings}**", f"**Wow !** You searched the Garden and found **$ {earnings}**", f"**Lovely !** You searched the Garden and found **$ {earnings}**", f"**Your Lucky !** You searched the Garden and found **$ {earnings}**"]
    

    
    users[str(user.id)]["wallet"]
    users[str(user.id)]["wallet"] += earnings
    
        
    await ctx.send(random.choice(reply1))

    with open("mainbank.json", "w") as f:
        json.dump(users,f)
@pantry.error
async def pantry_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):

        em = discord.Embed(color = 0x00FFFF)
        em.add_field(name = "You Just Searched The Pantry...", value = f'This command is on cooldown, you can **Search The Pantry Again** after **{round(error.retry_after)//60} Minutues**')
        
        await ctx.send(embed = em)
@garden.error
async def garden_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):

        em = discord.Embed(color = 0x00FFFF)
        em.add_field(name = "You Just Searched The Garden...", value = f'This command is on cooldown, you can **Search The Garden Again** after **{round(error.retry_after)} Seconds**')
        
        await ctx.send(embed = em)
@client.command(name = "pocket")

async def hels(ctx):
    await open_account(ctx.author)

    user = ctx.author
    
    users = await get_bank_data()
    earnings = random.randint(10, 30)
    
    users[str(user.id)]["wallet"] += earnings
    
    with open("mainbank.json", "w") as f:
        json.dump(users,f)
        
    await ctx.send(f"Awesome ! You searched your Pocket and found **$ {earnings}**")



@client.command()
async def slowmode(ctx, seconds: int):
    if ctx.author.guild_permissions.manage_channels:
        if seconds == 0:
            await ctx.channel.edit(slowmode_delay=seconds)
            await ctx.send("Slowmode has been removed from this channel successfully")
        else:
                await ctx.channel.edit(slowmode_delay=seconds)
                await ctx.send(f"Slowmode of {seconds} seconds has been set in this channel succesfully")

@slowmode.error
async def slowmode_error(ctx,error):
    await ctx.send("Sorry ! You do not have the permission to use this command. Please contact Staff or Admin.")

    
@client.command(aliases=['m'])
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
    guild = ctx.guild
    muted_role = discord.utils.get(guild.roles,name="Muted")
    await member.add_roles(muted_role)

    await ctx.send(member.mention + " has been muted")

@mute.error
async def msd(ctx, member: discord.Member):
    await ctx.send("Sorry ! You do not have the permission to use this command. Please contact Staff or Admin." )

@client.command(aliases=['u'])
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    guild = ctx.guild
    muted_role = discord.utils.get(guild.roles,name="Muted")
    await member.remove_roles(muted_role)

    await ctx.send(member.mention + " has been unmuted")

emoji_dict = {
    u"\u2196": 0,
    u"\u2B06": 1,
    u"\u2197": 2,
    u"\u2B05": 3,
    u"\u23FA": 4,
    u"\u27A1": 5,
    u"\u2199": 6,
    u"\u2B07": 7,
    u"\u2198": 8
}

def make_grid_internals(grid):
    """Converts the normal grid list into human-readable version."""
    # Replace all values in the grid list with emojis
    new_grid = [":white_large_square:" if (not x)
                else ":regional_indicator_x:" if x == 1
                else ":o2:" if x == 2
                else "?"
                for x in grid]

    # Adds a new line every three emojis.
    return "\n".join("".join(new_grid[i:i + 3]) for i in range(0, len(new_grid), 3))


async def draw_grid(channel, grid, player1, player2, current_player):
    """Draws the initial grid of the game."""
    grid = make_grid_internals(grid)

    current_player = player1 if current_player == 1 else player2
    description = f"{player1.mention} vs. {player2.mention}\n{current_player.mention}'s turn!"

    embed = discord.Embed(title="Tic-Tac-Toe!", description=description, color=0xF0FFFF)
    embed.add_field(name="Grid", value=grid)

    return await channel.send(embed=embed)


async def edit_grid(message, grid, player1, player2, current_player):
    grid = make_grid_internals(grid)


    current_player = player1 if current_player == 1 else player2
    description = f"{player1.mention} vs. {player2.mention}\n{current_player.mention}'s turn!"

    embed = discord.Embed(title="Tic-Tac-Toe!", description=description, color=0xF0FFFF)
    embed.add_field(name="Grid", value=grid)

    await message.edit(embed=embed)


async def edit_grid_end(message, grid, player1, player2, current_player, end_message):
    grid = make_grid_internals(grid)

    current_player = player1 if current_player == 1 else player2
    description = f"{player1.mention} vs. {player2.mention}\n{end_message}"

    embed = discord.Embed(title="Tic-Tac-Toe!", description=description, color=0xF0FFFF)
    embed.add_field(name="Grid", value=grid)

    await message.edit(embed=embed)


def win_indexes(n):
    # Rows
    for r in range(n):
        yield [(r, c) for c in range(n)]
    # Columns
    for c in range(n):
        yield [(r, c) for r in range(n)]
    # Diagonal top left to bottom right
    yield [(i, i) for i in range(n)]
    # Diagonal top right to bottom left
    yield [(i, n - 1 - i) for i in range(n)]


def is_winner(board, decorator):
    n = len(board)
    for indexes in win_indexes(n):
        if all(board[r][c] == decorator for r, c in indexes):
            return True
    return False


def check_for_end(grid):
    if 0 not in grid:
        return "draw"
    elif is_winner([grid[i:i + 3] for i in range(0, len(grid), 3)], 1):
        return 1
    elif is_winner([grid[i:i + 3] for i in range(0, len(grid), 3)], 2):
        return 2
    else:
        return


@client.command()
async def ps5(ctx, player2: commands.MemberConverter):
    """Starts a Tic-Tac-Toe game with the specified player!"""
    player1 = ctx.author
    current_player = 1
    running = True
    used_emojis = []

    # Makes sure that the player isn't a bot.
    if player2.bot:
        await ctx.send("You can't play against a bot!")
        return

    # Creates and sends the initial grid
    grid = [0 for x in range(9)]
    message = await draw_grid(ctx.channel, grid, player1, player2, current_player)

    # Adds all the emojis to make moves
    for emoji in emoji_dict:
        await message.add_reaction(emoji)

    # Running loop, continuously checks for new inputs until someone wins
    while running:
        # Makes a usable object based on current player
        current_player_object = player1 if current_player == 1 else player2

        def check(r, u):
            # Checks that it is a valid emoji, that the emoji wasn't used before, and that it is the current player
            return (r.emoji in emoji_dict) and (r.emoji not in used_emojis) and (u == current_player_object)

        # Waits for a reaction, edits grid and used emojis accordingly
        reaction, user = await client.wait_for("reaction_add", check=check)
        grid[emoji_dict[reaction.emoji]] = 1 if current_player == 1 else 2 if current_player == 2 else "??"
        used_emojis.append(reaction.emoji)

        end = check_for_end(grid)
        if end == "draw":
            await edit_grid_end(message, grid, player1, player2, current_player, "It's a draw!")
            running = False
        elif end == 1:
            await edit_grid_end(message, grid, player1, player2, current_player, f"{player1.mention} has won!")
            running = False
        elif end == 2:
            await edit_grid_end(message, grid, player1, player2, current_player, f"{player2.mention} has won!")
            running = False
        else:
            # Switch current player to next player
            current_player = 2 if current_player == 1 else 1

            # Update grid with new information
            await edit_grid(message, grid, player1, player2, current_player)

client.run('')
