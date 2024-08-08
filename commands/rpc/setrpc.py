from discord.ext import commands
import discord

@commands.command()
async def setrpc(ctx, *, activity: str = None):
    """Définit le RPC (Rich Presence) du bot."""
    if not activity:
        await ctx.send("Veuillez fournir le type et le nom de l'activité. Ex : setrpc playing Fortnite")
        return

    try:
        activity_type, activity_name = activity.split(' ', 1)
    except ValueError:
        await ctx.send("Format invalide. Utilisez le format : setrpc <type> <nom>. Ex : setrpc playing Fortnite")
        return

    activity_type = activity_type.lower()
    if activity_type == "playing":
        await ctx.bot.change_presence(activity=discord.Game(name=activity_name))
        await ctx.send(f"RPC défini à : {activity_type} {activity_name}")
    elif activity_type == "streaming":
        url = "http://twitch.tv/yourchannel"  # Remplacez cette URL par l'URL de votre choix
        await ctx.bot.change_presence(activity=discord.Streaming(name=activity_name, url=url))
        await ctx.send(f"RPC défini à : {activity_type} {activity_name}. Cliquez sur le profil pour accéder au streaming.")
    else:
        await ctx.send("Type d'activité non valide. Utilisez 'playing' ou 'streaming'.")
        return

async def setup(bot):
    bot.add_command(setrpc)
