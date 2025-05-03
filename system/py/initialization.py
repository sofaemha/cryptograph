from dotenv import load_dotenv as load_env

load_env()

from system.py.core import *
from system.controller.file import file
from system.controller.log import log
from system.controller.folder import folder
