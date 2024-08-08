from discord.ext import commands
import os
from dotenv import set_key, load_dotenv
import discord

load_dotenv()

@commands.command()
async def autojoin(ctx, channel_id: int = None):
    """Définit un canal vocal pour rejoindre automatiquement au démarrage du bot."""
    if channel_id is None:
        return await ctx.send("Veuillez fournir un ID de canal vocal.")
    
    channel = ctx.bot.get_channel(channel_id)
    if channel is None or not isinstance(channel, discord.VoiceChannel):
        return await ctx.send("L'ID spécifié ne correspond pas à un canal vocal valide.")

    env_file = '.env'
    set_key(env_file, "AUTOJOIN_CHANNEL_ID", str(channel_id))
    await ctx.send(f'ID du canal vocal pour autojoin défini à : {channel.mention}')

async def setup(bot):
    bot.add_command(autojoin)
