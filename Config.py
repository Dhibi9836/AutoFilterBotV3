import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('LuciferMoringstar_Robot')
API_ID = int(environ[5530754])
API_HASH = environ['5e51ecf5945605c711fffe7b376fa2a8']
BOT_TOKEN = environ['5694714864:AAHBWW5y2eZ-6xyGuygZOxhLWV5CxaA40HU
']

# Bot settings
CACHE_TIME = int(environ.get(300))
USE_CAPTION_FILTER = bool(environ.get(False))

BROADCAST_CHANNEL = int(os.environ.get(-1001865920944))
ADMIN_ID = set(int(x) for x in os.environ.get(1170610542).split())
DB_URL = os.environ.get("mongodb+srv://123:123@cluster1.7wqy6xv.mongodb.net/?retryWrites=true&w=majority")
BROADCAST_AS_COPY = bool(os.environ.get(True))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ[1170610542].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ[-1001594114982].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get().split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get(-1001696170170)
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get().split()]
TUTORIAL = "https://youtu.be/5hnYOKBzyi8"
# MongoDB information
DATABASE_URI = environ[]
DATABASE_NAME = environ['LuciferMoringstar_Robot']
COLLECTION_NAME = environ.get('channel_files')

# Messages
default_start_msg = """
**Hi, I'm Moviez Bot 4**

Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "http://www.omdbapi.com/?i=tt3896198&apikey=4f08a979")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
