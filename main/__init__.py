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
API_ID = 7498895
API_HASH = "5204d72f395c291b7257df9631a659ee"
BOT_TOKEN = "6147237683:AAHbwDk5AOBpcyIsm0EsHd-Ks0EWg9nxFIw"
SESSION = "BQCrXh9hBLCwEHH6DfBZ8m0DWphjw-I6SnoHaC61DxWV286rCHrGmRwPcl_hEOaCi057cAooVT-qNo6sFkfpgC39pUY9LLelziT2BGekSGaKnW2dz0lGTzKE5jdjPSRDWsPVzkQMbOwINgFCOIh0l4tDpJJqT_CynSIwOoD4r9yF-gNnQQVFBgwFebEOPoR3sQWk2AZZweHncKbEhOf4GM3dZ3U2funegNpf09crS4YnN7b3lZrJxs_hw9GoBi32EVE4cTIJeyUTlsjEIi1Bisf6Dt-IeeRFUBekDXiz93pcCusF3_tvXjICNHUYUmEDkVnwTKjXwWMteiD50e31oSd2AAAAAUaS2OoA"
FORCESUB = "KASHIRBOTS_premium"
AUTH = 5478996202
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
