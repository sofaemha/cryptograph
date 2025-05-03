from system.py.core import system, process
from system.controller.log import log


def tkintertheme(status):
    # Check if tkinter theme is installed, if not, install it.
    if status:
        log.write("TKinterModernThemes is already installed.")
    else:
        log.write("TKinterModernThemes is not installed. Installing...")
        process.check_call(
            [system.executable, "-m", "pip", "install", "TKinterModernThemes"]
        )
        log.write("TKinterModernThemes installed successfully.")
        log.write("Please restart application first.")
