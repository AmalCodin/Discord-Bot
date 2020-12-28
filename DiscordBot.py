import discord

client = discord.Client()

@client.event

async def on_ready():

    general_channel = client.get_channel(792913689292308493)
    await general_channel.send('Hello, People')

@client.event

async def on_message(message):

    if message.content == "what is the version":
        general_channel = client.get_channel(792913689292308493)

        myEmbed = discord.Embed(title="Current Version", description="The bot is in version 1.0", color=0x00ff00)
        myEmbed.add_field(name="Version Code:", value="Version 1.0", inline=False)
        myEmbed.add_field(name="Date Released", value="July 18th, 2020", inline=False)
        myEmbed.set_footer(text="This is a sample footer")
        myEmbed.set_author(name="Amal S")


        await general_channel.send(embed=myEmbed)

@client.event

async def on_disconnect():
    general_channel = client.get_channel(792913689292308493)

    await general_channel.send('GoodBye!')




client.run('NzkyNzg3OTQzNDEyMDcyNDQ4.X-izTg.Kz_S_Umx0h2Orqrgs4HL7aIkpLo')