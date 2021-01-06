import discord
from discord.ext import commands
import random 
import discord as d
from discord.utils import get
import asyncio
import requests
from discord import Member, Embed
from discord.ext.commands import command, cooldown, BucketType, CommandOnCooldown
client = commands.Bot(command_prefix = "--")

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
        await channel.send("City not found.")

@client.command(name='version')
async def version(context):

    myEmbed = discord.Embed(title="Current Version", description="The bot is in version 1.0", color=0x00ff00)
    myEmbed.add_field(name="Version Code:", value="Version 1.0", inline=False)
    myEmbed.add_field(name="Date Released", value="July 18th, 2020", inline=False)
    myEmbed.set_footer(text="Hope you got to know about its version ^_^")
    myEmbed.set_author(name="Amal S")

    await context.message.channel.send(embed=myEmbed)


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
        await ctx.send(f"Successfully given {role.mention} to {user.mention}.")
    else:
        await ctx.send("Sorry ! You do not have the permission to use this command. Please contact Staff or Admin.")


@client.command()
async def removerole(ctx, role: discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.manage_roles:
        await user.remove_roles(role)
        await ctx.send(f"Successfully removed {role.mention} to {user.mention}.")
    else:
        await ctx.send("Sorry ! You do not have the permission to use this command. Please contact Staff or Admin.")

@client.event

async def when_online():

    general_channel = client.get_channel(792913689292308493)
    await general_channel.send('Hello, People')

@client.event
async def on_message(message):

    if message.content == "what is the version":
        general_channel = client.get_channel(795101474627256360)

        myEmbed = discord.Embed(title="Current Version", description="The bot is in version 1.0", color=0x00ff00)
        myEmbed.add_field(name="Version Code:", value="Version 1.0", inline=False)
        myEmbed.add_field(name="Date Released", value="January 10th, 2021", inline=False)
        myEmbed.set_footer(text="This is a sample footer")
        myEmbed.set_author(name="Arcel")


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
         await context.send('User ' + member.display_name + ' has been banned')
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
        await ctx.send("You already have a support channel open. Kindly wait for your current support channel to be closed !")



@client.command()
async def close(ctx, member: discord.Member): 
    guild = ctx.guild
    channel = discord.utils.get(ctx.guild.channels, name='support-channel')
    nbed = d.Embed(
        title = 'Success',
        description = 'Support Channel:  has been closed !',
    )
    if ctx.author.guild_permissions.manage_channels:
        general = discord.utils.get(guild.text_channels, name="study-bot")
        await ctx.send(embed=nbed)
        await channel.delete()
        await general.send(f'Hi! {member.mention} Your support channel has been closed by one of the staff to open a new ticket please do --ticket again. Thank You')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('How to be a bot'))

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

client.run('NzkyNzg3OTQzNDEyMDcyNDQ4.X-izTg.KCa-WxhsP25x0myh2xHgt38ZknI')
