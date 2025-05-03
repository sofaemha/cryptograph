from system.py.core import system, process
from system.controller.log import log


def pycryptodome(status):
    # Check if pycryptodome is installed, if not, install it.
    if status:
        log.write("PyCryptodome is already installed.")
    else:
        log.write("PyCryptodome is not installed. Installing...")
        process.check_call([system.executable, "-m", "pip", "install", "pycryptodome"])
        log.write("PyCryptodome installed successfully.")
        log.write("Please restart application first.")
