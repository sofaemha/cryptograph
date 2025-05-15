from PIL import ImageTk, Image
from system.py.core import date
from system.py.tk import tk, tkt

import view.app.about as about
import view.app.encrypt as encrypt
import view.app.decrypt as decrypt
import view.app.member as member


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

        image_dark = ImageTk.PhotoImage(Image.open("view/image/logo-b.png").resize((200, 113)))
        image_light = ImageTk.PhotoImage(Image.open("view/image/logo-w.png").resize((200, 113)))
        if self.mode == "light":
            self.paneTop.Label("", widgetkwargs={"image": image_dark})
        else:
            self.paneTop.Label("", widgetkwargs={"image": image_light})

        self.menuFrame = self.paneTop.addLabelFrame("Data")
        self.menuFrame.AccentButton("Encrypt", command=self.execute, args=(encrypt,))
        self.menuFrame.AccentButton("Decrypt", command=self.execute, args=(decrypt,), col=1)

        self.systemFrame = self.paneTop.addLabelFrame("System")
        self.systemFrame.AccentButton("Member", command=self.execute, args=(member,))
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
