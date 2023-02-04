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
SESSION = "BQBA8kkN_L8jzlnoZDMK2V4Jg6sEgg3VH4XN5CrUSSgw8E47QIlskUIVdo6FpzhQiBxcqYmcXeRytdR5XxTQr4qhmmrUTnztvxeA7JEWFPppX_ky205PcxcTE3QT6TojGHdbJusyWI7vFq48msS_Hcgw-TDQgAdg4ZLXpf9MospARfmnXwkedfDQuH0xF4A0toKe0qoZEvfqiwKDHysAIjKnmXr4pMqZmB7jf_mN7pHfKPID0poZkw6bZiFaaA713CbKCus9k4cMox1XwRTLtDmrP6TrrIUrKaPf5dxr-MOs18PxchPuuTSo3-yDVi39gC4WlJr3212-L5ZF-oYA376_AAAAAUaS2OoA"
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
