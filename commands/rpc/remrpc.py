from discord.ext import commands
import discord

@commands.command()
async def remrpc(ctx):
    """Supprime le RPC actuel."""
    await ctx.bot.change_presence(activity=None)
    await ctx.send("RPC actuel supprimé.")

async def setup(bot):
    bot.add_command(remrpc)
