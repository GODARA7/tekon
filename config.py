import os

API_ID = API_ID =  20047839

API_HASH = os.environ.get("API_HASH", "e635f85a4dae812a26c450c0d41276b0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7417717621:AAFibMWs3uejBzUPJrljDww0zPq7NyQQo1M")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", "6332321765" ))

LOG = -1002116155974,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6332321765").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


