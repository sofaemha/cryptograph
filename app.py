from system.py.initialization import *
from system.py.library import library
from view.route import route


class App:
    @staticmethod
    def setup():
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
            system.exit(1)

    def start(self):
        route.root()
        print("Starting the application...")


if __name__ == "__main__":
    app = App()
    app.setup()
    app.start()
