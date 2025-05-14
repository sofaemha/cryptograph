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

        self.usecommandargs = tk.BooleanVar(value=True)
        self.usethemeconfigfile = tk.BooleanVar(value=True)
        self.memberFrame = None
        self.systemFrame = None

        self.panedWindow = self.PanedWindow("Paned Window Test")

        self.paneTop = self.panedWindow.addWindow()
        self.paneTop.Label("AES File Locker", colspan=2)

        self.member()

        self.paneBottom = self.panedWindow.addWindow()
        self.paneBottom.Label(f"All Rights Reserved \u00A9 {date.now().year}", size=10, weight="normal")

        self.run()

    def member(self):
        self.memberFrame = self.paneTop.addLabelFrame("Daftar Anggota")
        self.memberFrame.Text(
            "1. Sofa Machabba Haeta \n"
            "2. Adel Nayyan Amiva \n"
            "3. Muhammad Helmy Fadhillah \n"
        )

    def system(self):
        self.systemFrame = self.paneTop.addLabelFrame("System")
        self.systemFrame.AccentButton("Kembali", self.handleExit, widgetkwargs={"width": 45})
