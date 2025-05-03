from system.controller.log import log
from system.controller.sonner import sonner


def tkinter(status):
    # Check if pycryptodome is installed, if not, install it.
    if status:
        log.write("Tkinter is already installed.")
    else:
        log.write("Install tkinter manually, based on user platform first...")
        sonner.ubuntu_library()
