#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = 29409646
API_HASH = "a69d0340a520c1913c517bea143a3de7"
BOT_TOKEN = "5870879185:AAGZrye09-kxmJsmSa-rSqKT38FPoyfbgW8"
SESSION = "BQB8a3KQ1HsM1YfNU-1AIk9meM2P1ZQo_nCK3Mk1xmbiy3mtnNNuGOE7i77AGOBjhpkfr5aCAUYsUXCDOotd9eXHW-bDfSWF_cZRFS7YDCuzExHLnxMIb8aLjJMdnTqQS7iXynb-ciNP0I5_PDBzvWDilBzH857Xz4LeT1Gdt2hya671KPq4RrEy01dUsGpEWVNw6oC8_R_juseA1sS0Qump9KaPHHdgqtd0wC8iTFD4Lx6nFA8WG61CSUCcJXWSSf4ql9gipDetAxNKo0t8VPzYokNszt-13Ulkin3C-GjP6Orqu2c7qvkL0ronvBlIITRJKWkItEkKnhZTxLTtwLjTAAAAAUuyxcIA"
FORCESUB = "SK_MoviesOffl"
AUTH = 5564974530
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

#userbot = Client(
#    session_name=SESSION, 
#    api_hash=API_HASH, 
#    api_id=API_ID)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
