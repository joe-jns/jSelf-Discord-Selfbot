from discord.ext import commands

@commands.command()
async def leavevc(ctx):
    """Fait quitter le bot du canal vocal."""
    if ctx.voice_client is None:
        return await ctx.send("Le bot n'est pas connecté à un canal vocal.")
    else:
        try:
            await ctx.voice_client.disconnect()
            return await ctx.send("Le bot a quitté le canal vocal.")
        except Exception as e:
            return await ctx.send(f"Une erreur s'est produite en quittant le canal vocal : {e}")

async def setup(bot):
    bot.add_command(leavevc)
