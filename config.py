from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "24614078"))
API_HASH = getenv("API_HASH", "d16556719d9acafd4d5b4c7474d99384")
BOT_TOKEN = getenv("BOT_TOKEN", "6130274070:AAEZQzI25-U_zgiY3O3w3RomjfaFmvtujOg")
SESSION_NAME = getenv("SESSION_NAME", "AgBP69DpaqOlYZk80reIbzT_-0RIMchi7h5pAEyCKIIFziwP6Kt88ubXxBuE5YATWj-hbZJZ-Ri9uBW95r8f6GaN3PetBb5fQ22_qk7oFFlQe0R5xJiwSJz3vHnHO5olxEeLrbj0f--d_JhitRJC-cOf7gRz8xfMZAljcjn_dnyiOPWXszK40x9nO4roTmWiJNd605VZOT9tL0rDf-EjXctDHN6jC5PiikYMKpilWlnFlK4ZMIS_wWM9wy-AA6sjP9bC5umcuds82NzP7S043wcWU5EIT19ccqehK2G30Uv-7AO28vuIoaFJNUIO9z5VGRaci-Ngpgi9UZOMjNwK6uKsAAAAAWe8bEoA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "U_K_11")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "U_K1bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "EVOMAFIA")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "EVOMAFIA")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
