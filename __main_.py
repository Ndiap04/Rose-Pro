import importlib
import time
from pyrogram import idle
from uvloop import install
from roselibs import logging, BOT_VER, __version__ as gver
from Rose import LOGGER, LOOP, aiosession, bot1, bots, app, ids
from config import CMD_HNDLR, BOTLOG_CHATID
from Rose.modules import ALL_MODULES
from Rose.modules.basic.heroku import rose_log


MSG_ON = """
**Rose-Pro Userbot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
**Userbot Version -** `{}`
**Rose Libary Version - `{}`**
**Ketik** `{}rose` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
©️2023 SM|Sukses Makmur PROJECT 
"""

async def main():
    await app.start()
    LOGGER("Rose").info("Loading Everything.")
    for all_module in ALL_MODULES:
        importlib.import_module("Rose.modules" + all_module)
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await logging(bot)
            await geez_log()
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, gver, CMD_HNDLR))
            except BaseException as a:
                LOGGER("Rose").warning(f"{a}")
            LOGGER("Rose").info("Startup Completed")
            LOGGER("Rose").info(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            LOGGER("Rose").info(f"{e}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Geez").info("Starting Rose-Pro Userbot")
    install()
    LOOP.run_until_complete(main())
