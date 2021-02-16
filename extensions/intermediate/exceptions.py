from asyncio.tasks import create_task


class DevError(Exception):
    pass


class UserError(Exception):
    def __init__(self, bot, ctx, message):
        self.bot = bot
        self.ctx = ctx
        create_task(send_reply(self, message))


class IncorrectArgsError(UserError):
    def __init__(self, bot, ctx):
        super().__init__(bot, ctx, "Error: You supplied an argument with no value!")

async def send_reply(self, message):
    await self.ctx.message.reply(message)
