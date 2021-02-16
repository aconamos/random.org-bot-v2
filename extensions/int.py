import requests
import argparse

from .intermediate.exceptions import UserError, IncorrectArgsError

from asyncio.tasks import create_task
from discord.ext import commands


class Int(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def cog_unload(self):
        """
        """
    
    def get_args(self, ctx):
        pos_args = {'min': ctx.args[2], 'max': ctx.args[3]}
        args = ctx.message.content.replace(f"{ctx.prefix}int {pos_args['min']} {pos_args['max']}", '')
        parser = argparse.ArgumentParser()
        parser.add_argument('--count', type=int, default=1)
        parser.add_argument('--cols', type=int, default=1)
        parser.add_argument('--base', type=str, default=10)
        try:
            return pos_args | vars(parser.parse_args(args.split()))
        except argparse.ArgumentError:
            raise IncorrectArgsError(self.bot, ctx)

    
    @commands.command()
    async def int(self, ctx, min, max):
        print(f'Int called! \n Min: {min} \n Max: {max} \n CTX message: {ctx.message.content}')
        if int(min) >= int(max):
            raise MinGreaterThanMaxError(self.bot, ctx)
        print(self.get_args(ctx))


def setup(bot):
    bot.add_cog(Int(bot))


class MinGreaterThanMaxError(UserError):
    def __init__(self, bot, ctx):
        super().__init__(bot, ctx, "Error: Your minimum value was greater than or equal to your maximum value!")