from aiogram import Bot
from aiogram.methods.set_my_commands import BotCommand
from aiogram.types import BotCommandScopeAllPrivateChats


async def set_default_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Botni ishga tushirish"),
        BotCommand(command="/help", description="Yordam: bot ishlamasa /start ni bosing."),
        BotCommand(command="/admin", description="Bu botni:\n Turobov Ozodbek va Sardorbek: ishga tushirdi "),

    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeAllPrivateChats())