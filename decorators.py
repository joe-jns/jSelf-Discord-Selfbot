import functools
import discord
from discord.ext import commands

def delete_command_message():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(ctx, *args, **kwargs):
            result = await func(ctx, *args, **kwargs)
            try:
                await ctx.message.delete()
            except discord.errors.Forbidden:
                pass  # The bot does not have permission to delete the message
            return result
        return wrapper
    return decorator

def auto_delete_reply(delay: int = 20):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(ctx, *args, **kwargs):
            result = await func(ctx, *args, **kwargs)
            if isinstance(result, discord.Message):
                try:
                    await result.delete(delay=delay)
                except discord.errors.Forbidden:
                    pass  # The bot does not have permission to delete the message
            return result
        return wrapper
    return decorator
