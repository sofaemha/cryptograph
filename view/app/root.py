from system.py.tk import tkt


class App(tkt.ThemedTKinterFrame):
    def __init__(self, theme, mode, usecommandlineargs=True, usethemeconfigfile=True):
        super().__init__(
            "AES-LF",
            theme,
            mode,
            usecommandlineargs=usecommandlineargs,
            useconfigfile=usethemeconfigfile,
        )

        self.frame = self.addLabelFrame("Main Menu")
        self.frame.AccentButton("Encrypt", command=self.debugPrint)

        self.debugPrint()
        self.run()
