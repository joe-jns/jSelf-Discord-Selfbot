from discord.ext import commands
import os
from dotenv import set_key

@commands.command()
async def prefix(ctx, new_prefix: str):
    """Change le préfixe des commandes pour ce serveur et le stocke dans le fichier .env"""
    env_file = '.env'
    set_key(env_file, "COMMAND_PREFIX", new_prefix)
    await ctx.send(f'Préfixe changé en : {new_prefix}')

async def setup(bot):
    bot.add_command(prefix)
