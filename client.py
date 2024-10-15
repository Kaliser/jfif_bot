import discord
from discord.ext import commands
import aiohttp
from io import BytesIO
from PIL import Image
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

DISCORD_BOT_TOKEN = config['discord']['token']
DISCORD_BOT_PREFIX = config['discord']['prefix']

# Make sure to enable the message content intent in your bot settings
intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix=DISCORD_BOT_PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} is now running!')

@bot.event
async def on_message(message):
    # prevent the bot from responding to its own messages
    if message.author == bot.user:
        return

    if message.attachments:
        for attachment in message.attachments:
            # check if the attachment is a .jfif image
            # might work for other container formats as well
            if attachment.filename.lower().endswith('.jfif'):
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(attachment.url) as resp:
                            if resp.status == 200:
                                data = await resp.read() # read image data
                            else:
                                await print(f"Failed to download the image. Status code: {resp.status}")
                                return

                    image = Image.open(BytesIO(data)).convert('RGB')

                    # we need BytesIO object to send the image back
                    with BytesIO() as image_binary:
                        image.save(image_binary, format='JPEG')
                        image_binary.seek(0)

                        # create a new filename with .jpg extension
                        new_filename = attachment.filename.rsplit('.', 1)[0] + '.jpg'

                        content = f'Converted .jfif posted by {message.author.name}'
                        # send the converted image back to the channel
                        await message.channel.send(content=content, file=discord.File(fp=image_binary, filename=new_filename))

                            
                except Exception as e:
                    await message.channel.send(f"An error occurred while processing the image")
                    print(f"An error occurred: {e}")

    # for if you have any command decorators
    await bot.process_commands(message)

bot.run(DISCORD_BOT_TOKEN)
