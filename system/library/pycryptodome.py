from system.py.core import system, process
from system.controller.log import log
from Crypto.Cipher import AES as aes
from Crypto.Random import get_random_bytes as random_bytes

def pycryptodome(status):
    # Check if pycryptodome is installed, if not, install it.
    if status:
        log.write("PyCryptodome is already installed.")
    else:
        log.write("PyCryptodome is not installed. Installing...")
        process.check_call([system.executable, "-m", "pip", "install", "pycryptodome"])
        log.write("PyCryptodome installed successfully.")
        log.write("Please restart application first.")
