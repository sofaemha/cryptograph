from dotenv import load_dotenv as load_env

load_env()

from system.py.core import *

FOLDER_PUBLIC = env("FOLDER_PUBLIC")
FILE_LOG = env("FILE_LOG")
os.makedirs("public", exist_ok=True)
open(f"{FOLDER_PUBLIC}{FILE_LOG}", "a").close()

from system.controller.file import file
from system.controller.log import log
from system.controller.folder import folder
