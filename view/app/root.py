from system.py.core import date
from system.py.tk import tk, tkt


class App(tkt.ThemedTKinterFrame):
    def __init__(self, theme, mode, usecommandlineargs=True, usethemeconfigfile=True):
        super().__init__(
            "AES File Locker",
            theme,
            mode,
            usecommandlineargs=usecommandlineargs,
            useconfigfile=usethemeconfigfile,
        )
        self.root.resizable(False, False)

        self.panedWindow = self.PanedWindow("Paned Window Test")

        self.paneTop = self.panedWindow.addWindow()
        self.paneTop.Label("AES File Locker", colspan=2)

        self.menuFrame = self.paneTop.addLabelFrame("Data")
        self.menuFrame.AccentButton("Encrypt", command=self.debugPrint)
        self.menuFrame.AccentButton("Decrypt", command=self.debugPrint, col=1)
        self.menuFrame.AccentButton("Clear Data", command=self.debugPrint, colspan=2)

        self.systemFrame = self.paneTop.addLabelFrame("System")
        self.systemFrame.AccentButton("Setting", command=self.debugPrint)
        self.systemFrame.AccentButton("About", command=self.debugPrint, col=1)
        self.systemFrame.AccentButton("Exit", command=self.handleExit, colspan=2)

        self.paneBottom = self.panedWindow.addWindow()
        self.paneBottom.Label(f"All Rights Reserved \u00A9 {date.now().year}", size=10, weight="normal")

        self.run()
