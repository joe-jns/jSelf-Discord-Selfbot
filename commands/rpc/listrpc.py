from discord.ext import commands

@commands.command()
async def listrpc(ctx):
    """Affiche la liste des types de RPC disponibles."""
    rpc_list = """
    Types de RPC disponibles :
- playing : Jouer à un jeu (Ex : playing Fortnite)
- streaming : Streamer quelque chose (Ex : streaming sur Twitch)
    """
    await ctx.send(rpc_list)

async def setup(bot):
    bot.add_command(listrpc)
