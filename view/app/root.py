from system.py.core import date
from system.py.tk import tk, tkt

import view.app.about as about
import view.app.encrypt as encrypt


class App(tkt.ThemedTKinterFrame):
    def __init__(self, theme, mode, usecommandlineargs=True, usethemeconfigfile=True):
        super().__init__(
            "AES File Locker",
            theme,
            mode,
            usecommandlineargs=usecommandlineargs,
            useconfigfile=usethemeconfigfile,
        )

        self.usecommandargs = tk.BooleanVar(value=True)
        self.usethemeconfigfile = tk.BooleanVar(value=True)

        self.root.resizable(False, False)

        self.panedWindow = self.PanedWindow("Paned Window Test")

        self.paneTop = self.panedWindow.addWindow()
        self.paneTop.Label("AES File Locker", colspan=2)

        self.menuFrame = self.paneTop.addLabelFrame("Data")
        self.menuFrame.AccentButton("Encrypt", command=self.execute, args=(encrypt,))
        self.menuFrame.AccentButton("Decrypt", command=self.debugPrint, col=1)
        self.menuFrame.AccentButton("Clear Data", command=self.debugPrint, colspan=2)

        self.systemFrame = self.paneTop.addLabelFrame("System")
        self.systemFrame.AccentButton("Setting", command=self.debugPrint)
        self.systemFrame.AccentButton("About", command=self.execute, args=(about,), col=1)
        self.systemFrame.AccentButton("Exit", command=self.handleExit, colspan=2)

        self.paneBottom = self.panedWindow.addWindow()
        self.paneBottom.Label(f"All Rights Reserved \u00A9 {date.now().year}", size=10, weight="normal")

        self.run()

    def execute(self, show):
        self.root.withdraw()
        show.App(self.theme, self.mode, self.usecommandargs.get(), self.usethemeconfigfile.get())
        self.root.update()
        self.root.deiconify()
