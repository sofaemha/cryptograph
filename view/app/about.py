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
        self.descFrame = None
        self.featureFrame = None
        self.systemFrame = None

        self.panedWindow = self.PanedWindow("Paned Window Test")

        self.paneTop = self.panedWindow.addWindow()
        self.paneTop.Label("AES-FL : About", colspan=2)

        self.description()
        self.feature()
        self.system()

        self.paneBottom = self.panedWindow.addWindow()
        self.paneBottom.Label(f"All Rights Reserved \u00A9 {date.now().year}", size=10, weight="normal")

        self.run()

    def description(self):
        self.descFrame = self.paneTop.addLabelFrame("Pengertian")
        self.descFrame.Text(
            "AESFileLocker adalah aplikasi Python yang digunakan \n"
            "untuk mengenkripsi dan mendekripsi file teks menggunakan \n"
            "Advanced Encryption Standard (AES). Aplikasi ini dirancang \n"
            "bagi pengguna yang ingin menyimpan file sensitif secara aman \n"
            "di komputer pribadi."
        )

    def feature(self):
        self.featureFrame = self.paneTop.addLabelFrame("Fitur")
        self.featureFrame.Text(
            "1. Enkripsi dan Dekripsi File Teks (.txt)\n"
            "2. Antarmuka Pengguna yang Ramah\n"
            "3. Keamanan Tingkat Tinggi\n"
            "4. Input Kunci dari Pengguna\n"
        )

    def system(self):
        self.systemFrame = self.paneTop.addLabelFrame("System")
        self.systemFrame.AccentButton("Kembali", self.handleExit, widgetkwargs={"width": 45})
