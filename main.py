import discord
from discord.ext import commands
from PIL import Image
from ai import detect_bird

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowales sie jako {bot.user}')

@bot.command()
async def receive(ctx):
    if len(ctx.message.attachments) > 0:
        for attachment in ctx.message.attachments:
            print(attachment.filename)
            print(attachment.url)
            file_path = f"./downloaded_files/{attachment.filename}"
            await attachment.save(file_path)
            image=Image.open(file_path)
            detected_class = detect_bird("model\keras_model.h5", "model\labels.txt", image)
            await ctx.send(f"Na zdjęciu widać {detected_class[0]}")
    else:
        await ctx.send("Nie wysłałeś żadnego obrazka!")

bot.run("")