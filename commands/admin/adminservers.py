from discord.ext import commands

@commands.command()
async def adminservers(ctx):
    """Affiche la liste des serveurs où vous avez les permissions administratives et le nombre de membres."""
    admin_servers = []
    for guild in ctx.bot.guilds:
        member = guild.get_member(ctx.bot.user.id)
        if member.guild_permissions.administrator:
            admin_servers.append((guild.name, guild.member_count))

    if not admin_servers:
        await ctx.send("Vous n'avez pas de permissions administratives dans aucun serveur.")
        return

    response = "Voici la liste des serveurs où vous avez les permissions administratives :\n\n"
    for server_name, member_count in admin_servers:
        response += f"**{server_name}** - {member_count} membres\n"

    await ctx.send(response)

async def setup(bot):
    bot.add_command(adminservers)
