import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DEFAULT_PREFIX = os.getenv('COMMAND_PREFIX')
AUTOJOIN_CHANNEL_ID = os.getenv('AUTOJOIN_CHANNEL_ID')

# Fonction pour obtenir le préfixe
def get_prefix(bot, message):
    return os.getenv('COMMAND_PREFIX', DEFAULT_PREFIX)

# Initialiser le bot
bot = commands.Bot(command_prefix=get_prefix, self_bot=True)

async def load_commands(bot):
    for folder in os.listdir('./commands'):
        folder_path = os.path.join('./commands', folder)
        if os.path.isdir(folder_path):
            for filename in os.listdir(folder_path):
                if filename.endswith('.py') and not filename.startswith('__'):
                    extension = f'commands.{folder}.{filename[:-3]}'
                    try:
                        await bot.load_extension(extension)
                        print(f"Loaded {extension} successfully.")
                    except Exception as e:
                        print(f"Failed to load extension {extension}: {e}")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}!')
    await load_commands(bot)

    # Rejoindre automatiquement le canal vocal si AUTOJOIN_CHANNEL_ID est défini
    if AUTOJOIN_CHANNEL_ID:
        channel = bot.get_channel(int(AUTOJOIN_CHANNEL_ID))
        if channel and isinstance(channel, discord.VoiceChannel):
            try:
                await channel.connect()
                print(f"Auto-joined channel: {channel.name}")
            except discord.errors.Forbidden:
                print("Permissions insuffisantes pour rejoindre le canal vocal.")
            except discord.errors.HTTPException as e:
                print(f"Une erreur s'est produite en rejoignant le canal vocal : {e}")
            except Exception as e:
                print(f"Une erreur inattendue s'est produite : {e}")
        else:
            print("ID de canal vocal autojoin invalide ou canal introuvable.")

@bot.event
async def on_command_completion(ctx):
    try:
        await ctx.message.delete()
    except discord.errors.Forbidden:
        pass  # The bot does not have permission to delete the message
    except Exception as e:
        print(f"Error deleting message: {e}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        try:
            await message.delete(delay=20)
        except discord.errors.Forbidden:
            pass  # The bot does not have permission to delete the message
        except Exception as e:
            print(f"Error deleting bot message: {e}")

    await bot.process_commands(message)

bot.run(TOKEN)
