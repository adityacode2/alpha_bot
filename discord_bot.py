# import discord
# import openai

# openai.api_key = "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"

# client = discord.Client(intents=discord.Intents.all())

# # Replace CHANNEL_NAME with the name of the channel you want the bot to respond in
# CHANNEL_NAME = "chat-bot"

# @client.event
# async def on_ready():
#     print("Logged in as {0.user}".format(client))

# @client.event
# async def on_message(message):
#     # Only respond to messages in the specified channel
#     if message.channel.name != CHANNEL_NAME:
#         return

#     # Check if the message starts with the desired command string
#     if not message.content.startswith("/ask"):
#         return

#     # Remove the command string from the message content
#     message_content = message.content[5:]  # 5 is the length of the command string "/ask "

#     if message.author == client.user:
#         return

#     prompt = (f"{message.author.mention} asked: {message_content}\n")
#     response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024, temperature=0.5)
#     result = response["choices"][0]["text"]
#     # Create a new thread to send the bot's response
#     async with message.channel.typing():
#         new_thread = await message.channel.send(result)
#         await new_thread.add_reaction("✅")


# client.run("MTA1OTQ2OTI3Nzg2ODA2ODk0NA.GJet5i.hgrlsBKRE3tiWPyFOZhL62wMbdX65DFxxExbJo")

import discord
import openai
from discord.ext import commands

openai.api_key = "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"

client = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(command_prefix='>', client=client, intents=discord.Intents.all())

# Replace CHANNEL_NAME with the name of the channel you want the bot to respond in
CHANNEL_NAME = "chat-bot"

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    # Only respond to messages in the specified channel
    if message.channel.name != CHANNEL_NAME:
        return

    # Check if the message starts with the desired command string
    if not message.content.startswith(">gpt"):
        return

    # Remove the command string from the message content
    message_content = message.content[5:]  # 5 is the length of the command string ">gpt"

    if message.author == client.user:
        return

    # Get the name of the user who asked the question
    user_name = message.author.name
    # Use string formatting to include the name of the user in the prompt
    prompt = (f"{user_name} asked: {message_content}\n")
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024, temperature=0.5)
    result = response["choices"][0]["text"]
    # Create a new thread to send the bot's response
    async with message.channel.typing():
        # Create an Embed object and set the title and description
        embed = discord.Embed(title=f"{user_name} asked:", description=result)

        # Send the Embed object as the message
        await message.channel.send(embed=embed)

@bot.command()
async def gpt(ctx, *, message):
    # Get the name of the user who asked the question
    user_name = message.author.name
    # Use string formatting to include the name of the user in the prompt
    prompt = (f"{user_name} asked: {message_content}\n")
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024, temperature=0.5)
    result = response["choices"][0]["text"]

    # Create an Embed object and set the title and description
    embed = discord.Embed(title=f"{user_name} asked:", description=result)

    # Send the Embed object as the message
    await ctx.send(embed=embed)


client.run("MTA1OTQ2OTI3Nzg2ODA2ODk0NA.GJet5i.hgrlsBKRE3tiWPyFOZhL62wMbdX65DFxxExbJo")