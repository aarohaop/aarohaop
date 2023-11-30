# ©️ DKBOTZ or https://t.me/DKBOTZ
# Coded By https://t.me/DKBOTZHELP 
# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", '21159773')) #API ID from https://my.telegram.org/auth
API_HASH = os.environ.get("API_HASH", '49ae08543a07335e195756eba2f56e11') #API Hash from https://my.telegram.org/auth
BOT_TOKEN = os.environ.get("BOT_TOKEN", '6538568462:AAEKlmAr7br3KRtmUVCD6sH6jWsArokT5k8') # Bot token from @BotFather
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split(",")] if os.environ.get("5886772061") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", 'SHARE')
DATABASE_URL = os.environ.get("DATABASE_URL", 'mongodb+srv://SK:SK@cluster0.hbkrl.mongodb.net/?retryWrites=true&w=majority') # mongodb uri from https://www.mongodb.com/
OWNER_ID =  int(os.environ.get("OWNER_ID", '5886772061')) # id of the owner
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5886772061)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002050926827")) # log channel for information about users
UPDATE_CHANNEL = int(os.environ.get("UPDATE_CHANNEL", "tech_support_channel")) # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start
LINK_BYPASS = "True" 


# SHORTNER

SHORTNER_LINK = os.environ.get("SHORTNER_LINK", 'ez4short.xyz')
CHANNEL_LINK = os.environ.get("CHANNEL_LINK", 'https://t.me/EZ4short_official')
