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
BOT_TOKEN = "5931678308:AAELiv12VQ9itTkyevoZ-7DlowOHBysxUjU"
SESSION = "AQAYE4IFXO0SjiKDKlwhmYLaTIFCkNq1LHENlT8DExAIphz0ibtjpupxNTKqVNei10_Z4OsHpSJinRPaq4dGTDmEqzPyV1l78jBNKgu1Yv5wd-VddiczExq8TQqfgO3K4pn8zf8PSbItUAkmNSsYN9daJeQW3xW1H_Q9S22SIgvXu902r4WyeYo96GNMyz8A4MGO1prt0V6PwnANctf94_YQTp95Xz2JkQ6J4peJNic8pKZG5qbt1ln3QoRFVVkELyJDZBZXx2iWZmDul-gyVsTPDZufqmEKvZmWl4tYxnybZPRBIvsjBd22k4ifQfScHs19mgrBhiNHooXMVrJUk5QaAAAAAV6vDl0A"
FORCESUB = "SK_MoviesOffl"
AUTH = 5883498077
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
