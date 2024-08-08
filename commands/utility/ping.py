from discord.ext import commands

@commands.command()
async def ping(ctx):
    """Affiche le ping du bot"""
    latency = round(ctx.bot.latency * 1000)
    await ctx.send(f'🏓 Pong! {latency}ms')

async def setup(bot):
    bot.add_command(ping)
