from system.py.initialization import *
from system.py.library import library
from system.controller.folder import folder
from view.route import route

PATH_ENCRYPT = env("PATH_ENCRYPT")
PATH_DECRYPT = env("PATH_DECRYPT")
FOLDER_PUBLIC = env("FOLDER_PUBLIC")


class App:
    @staticmethod
    def module():
        module = library.check()
        if module:
            log.write("All modules are installed.")
        else:
            log.write("Some modules are missing. Please install them manually.")
            system.exit()

    @staticmethod
    def setup():
        folder.create(PATH_ENCRYPT)
        folder.create(PATH_DECRYPT)

    def start(self):
        route.root()
        print("Starting the application...")


if __name__ == "__main__":
    app = App()
    app.setup()
    app.module()
    app.start()
