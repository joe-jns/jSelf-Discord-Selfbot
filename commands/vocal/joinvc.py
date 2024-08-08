from discord.ext import commands
import discord

@commands.command()
async def joinvc(ctx, channel_id: int = None):
    """Fait rejoindre le bot à un canal vocal spécifié par son ID."""
    if channel_id is None:
        return await ctx.send("Veuillez fournir un ID de canal vocal.")
    
    channel = ctx.bot.get_channel(channel_id)
    if channel is None or not isinstance(channel, discord.VoiceChannel):
        return await ctx.send("L'ID spécifié ne correspond pas à un canal vocal valide.")
    
    try:
        await channel.connect()
        return await ctx.send(f'Le bot a rejoint le canal vocal : {channel.mention}')
    except discord.errors.Forbidden:
        return await ctx.send("Le bot n'a pas les permissions nécessaires pour rejoindre ce canal vocal.")
    except discord.errors.HTTPException as e:
        return await ctx.send(f"Une erreur s'est produite en rejoignant le canal vocal : {e}")
    except Exception as e:
        return await ctx.send(f"Une erreur inattendue s'est produite : {e}")

async def setup(bot):
    bot.add_command(joinvc)
