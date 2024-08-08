from discord.ext import commands
import discord
import asyncio

class CustomHelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help', help='Affiche ce message')
    async def help_command(self, ctx, *args):
        category = args[0] if args else None
        help_text = "Voici les catégories disponibles. Utilisez `help <categorie>` pour voir les commandes dans une catégorie spécifique :\n\n"
        help_text += "**Catégories :**\n"

        categories = {
            'utility': 'Commandes utilitaires',
            'vocal': 'Commandes de salon vocal',
            'admin': 'Commandes administratives',
            'rpc': 'Commandes Rich Presence (RPC)'
        }

        if category:
            if category == 'utility':
                help_text = """
**Commandes utilitaires :**
- `ping` : Affiche le ping du bot.
- `prefix` : Change le préfixe des commandes pour ce serveur et le stocke dans le fichier .env
                """
            elif category == 'vocal':
                help_text = """
**Commandes de salon vocal :**
- `joinvc` : Fait rejoindre le bot à un canal vocal spécifié par son ID.
- `leavevc` : Fait quitter le bot du canal vocal.
- `autojoin` : Définit un canal vocal pour rejoindre automatiquement au démarrage du bot.
                """
            elif category == 'admin':
                help_text = """
**Commandes administratives :**
- `adminservers` : Affiche la liste des serveurs où vous avez les permissions administratives et le nombre de membres.
                """
            elif category == 'rpc':
                help_text = """
**Commandes Rich Presence (RPC) :**
- `setrpc` : Définit le RPC du bot. Ex : setrpc playing Fortnite
- `listrpc` : Affiche la liste des types de RPC disponibles.
- `remrpc` : Supprime le RPC actuel.
                """
        else:
            for cat, description in categories.items():
                help_text += f"- `{cat}` : {description}\n"

        confirmation_message = await ctx.send(help_text.strip())
        await self.delete_command_message(ctx.message)
        await self.delete_message_later(confirmation_message, delay=30)

    async def delete_message_later(self, msg, delay=30):
        await asyncio.sleep(delay)
        try:
            await msg.delete()
        except discord.errors.NotFound:
            pass
        except discord.errors.Forbidden:
            print("Permissions insuffisantes pour supprimer le message.")

    async def delete_command_message(self, cmd_message):
        if isinstance(cmd_message.channel, discord.DMChannel):
            return
        try:
            await cmd_message.delete()
        except discord.errors.NotFound:
            pass
        except discord.errors.Forbidden:
            print("Permissions insuffisantes pour supprimer le message de commande.")

async def setup(bot):
    bot.remove_command('help')  # Remove default help command
    await bot.add_cog(CustomHelpCommand(bot))
