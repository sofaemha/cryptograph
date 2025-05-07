from system.controller.sonner import sonner
from system.py.initialization import *
from system.py.library import library
from system.controller.folder import folder
from view.route import route

PATH_ENCRYPT = env("PATH_ENCRYPT")
PATH_DECRYPT = env("PATH_DECRYPT")
PATH_KEY = env("PATH_KEY")

class App:
    @staticmethod
    def module():
        # ! Module and function must be same order
        module = [
            "tkinter",
            "Crypto",
            "TKinterModernThemes",
        ]  # Modules name stored in `sys.modules`
        fn = [
            "tkinter",
            "pycryptodome",
            "tkintertheme",
        ]  # Functions to call on `system.library`
        status = library.check(module, fn)
        if not status:
            log.write("Some libraries are missing")
            sonner.ubuntu_library()
            system.exit(1)

    @staticmethod
    def setup():
        folder.create(PATH_ENCRYPT)
        folder.create(PATH_DECRYPT)
        folder.create(PATH_KEY)

    def start(self):
        route.root()
        print("Starting the application...")


if __name__ == "__main__":
    app = App()
    app.module()
    app.setup()
    app.start()
