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
async def on_messae(message):

    if message.content == "what is the version":
        general_channel = client.get_channel(795101474627256360)

        myEmbed = discord.Embed(title="Current Version", description="The bot is in version 1.0", color=0x00ff00)
        myEmbed.add_field(name="Version Code:", value="Version 1.0", inline=False)
        myEmbed.add_field(name="Date Released", value="January 10th, 2021", inline=False)
        myEmbed.set_footer(text="Hope you got it")
        myEmbed.set_author(name="Made By Arcel")


        await general_channel.send(embed=myEmbed)

    if message.content == 'send a DM':
        await message.author.send('Have a cheerful day ahead dear user! We love you')

    await client.process_commands(message)

@client.event

async def on_disconnect():
    general_channel = client.get_channel(792913689292308493)

    await general_channel.send('GoodBye!')

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
    await ctx.send('Sorry ! You do not have the permission to use this command. Please contact Staff or Admin.')

@client.command(name="radimg")
async def  randimg(context):
    images = ["Lmao.png", "LOL.png", "vvv.png", "vvvvvv.png", "vyttr.png"]

    random_image = random.choice(images)

    await context.send(file=discord.File(random_image))
@client.command()
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

filtered_words = ["Faggot","nigger","faggot", "Transvestite","twat","suicide","boob"," anal","bloody bitch", "asshole", "son of a bitch"]

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

mainshop = [{"name":"Watch","price":100,"description":"To Check Time"},
{"name":"Laptop","price":1000,"description":"Work Remotely"},
{"name":"Z-Box","price":6000,"description":"Gaming Console"},
{"name":"PS-5","price":10000,"description":"Better Gaming Console"}]

limited = [{"name": emoji.emojize("Arcelean Trophy  :trophy:"),"price": 100000,"description":"One of the best items you can have in the entire shop those who have this item are represented as the top honary people"}]
coin = [{"name": emoji.emojize("Supa Rare Coin  :coin:"),"price": 50000,"description":"The rarest unique coin obtainable. Users having this coin in their bag are truly special and have been very rich."}]
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
    
    for coins in coin:
        man = coins["name"]
        sam = coins["price"]
        lmao = coins["description"]
        em2.add_field(name = man, value = f"${sam} | {lmao}")

    await ctx.send(embed = em)
    await ctx.send(embed = em2)
@client.command()
async def shop(ctx):
    em = discord.Embed(title = "Shop:", color = 0x00ff00)
    em.set_thumbnail(url='https://images.unsplash.com/photo-1472851294608-062f824d29cc?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MXx8c2hvcHxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&w=1000&q=80')

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name = name, value = f"${price} | {desc}")

    await ctx.send(embed = em)




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

    await ctx.send(f"Contragulations ! You just bought {amount} {item}")

@client.command()
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []

    em = discord.Embed(title = f"{ctx.author}'s Bag", color = 0x00ff00)
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value= amount)
        em.set_thumbnail(url='https://media.giphy.com/media/McIZk48IDPC5Ndg27p/giphy.gif')


    await ctx.send(embed = em)

async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
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

@client.command()
async def lb(ctx, x = 3):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)

    em = discord.Embed(title = f"Top {x} Richest People:", description = "This is the list of the **Top 3 Richest People** in the game decided on the basis of the amount of money they have in both their wallet and bank.", color = 0x00ff00)

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


@client.command(name="withdraw", aliases = ["with", "w"])
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)


    amount = int(amount)

    if amount>bal[1]:
        await ctx.send("Sorry ! You do not have that much money to withdraw")
        return
    if amount<0:
        await ctx.send("Amount must be Positive !")

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,"bank")

    await ctx.send(f"You withdrew {amount} coins !")


@client.command()
async def dep(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Please enter the amount")
        return

    bal = await update_bank(ctx.author)


    amount = int(amount)

    if amount>bal[0]:
        await ctx.send("Sorry ! You do not have that much money to withdraw")
        return
    if amount<0:
        await ctx.send("Amount must be Positive !")

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,"bank")

    await ctx.send(f"You deposited {amount} coins !")

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
        await ctx.send("Sorry ! You do not have that much money to withdraw")
        return
    if amount<0:
        await ctx.send("Amount must be Positive !")

    await update_bank(ctx.author,-1*amount,"bank")
    await update_bank(member,amount,"bank")

    await ctx.send(f"You gave {amount} coins to {member}")

@client.command()
async def bet(ctx,amount = None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("Please enter the amount of money to bet")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount>bal[0]:
        await ctx.send(f"You do not have that much money in your wallet to place a bet of {amount} coins")
        return
    if amount<0:
        await ctx.send("Amount must be positive !")
        return

    final = []

    for a in range(3):
        a = emoji.emojize(random.choice([":o:",":x:",":red_circle:"]))

        final.append(a)

    await ctx.send(str(final))

    if final[0] == final[1] == final[2] or final[2] == final[1]:
        await update_bank(ctx.author,2*amount)
        await ctx.send(f"Contragulations ! You have won {2*amount} coins")
    else:
        await update_bank(ctx.author,-1*amount)
        await ctx.send(f"You lost {amount} coins")




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

    await ctx.send(f"You just sold {amount} {item}.")

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
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
async def slowmode(ctx, seconds: int):
    if seconds == 0:
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send("Slowmode has been removed from this channel successfully")
    else:
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.send(f"Slowmode of {seconds} seconds has been set in this channel succesfully")


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

client.run(' ')
