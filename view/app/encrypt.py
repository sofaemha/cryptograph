from system.library.pycryptodome import aes, random_bytes
from system.py.core import date, env
from system.controller.log import log
from system.controller.file import file
from system.py.tk import tk, tkt, getfile, alert
from system.controller.folder import folder

PATH_ENCRYPT = env("PATH_ENCRYPT")
PATH_DECRYPT = env("PATH_DECRYPT")
PATH_KEY = env("PATH_KEY")


class App(tkt.ThemedTKinterFrame):
    def __init__(self, theme, mode, usecommandlineargs=True, usethemeconfigfile=True):
        super().__init__(
            "AES File Locker",
            theme,
            mode,
            usecommandlineargs=usecommandlineargs,
            useconfigfile=usethemeconfigfile,
        )

        self.observer = None
        self.treeView = None
        self.treeData = None
        self.treeFolder = None
        self.treeRawFolder = None
        self.folder = folder
        self.getfile = getfile
        self.usecommandargs = tk.BooleanVar(value=True)
        self.usethemeconfigfile = tk.BooleanVar(value=True)

        self.root.resizable(False, False)

        self.panedWindow = self.PanedWindow("Paned Window Test")

        self.paneTop = self.panedWindow.addWindow()
        self.paneTop.Label("AES File Locker", colspan=2)

        self.treeFrame = self.paneTop.addLabelFrame("Data", rowspan=2)
        self.treeRawFolder = [f'{PATH_ENCRYPT}{filename}' for filename in self.folder.list(PATH_ENCRYPT)]
        self.treeFolder = [
            [f, file.timestamp(f"{"/".join(f.split("/")[:-1])}/", f.split("/")[-1])] for f in self.treeRawFolder
        ]
        self.treeData = [
            {"path": "public/encrypt/", "encrypt": f[0].split("/")[-1], "date": f[1]} for f in self.treeFolder
        ]
        self.treeView = self.treeFrame.Treeview(["Encrypt", "Date"], [120, 120], 5, self.treeData, None,
                                                ["encrypt", "date"])

        self.encryptFrame = self.paneTop.addLabelFrame("Enkripsi", col=1)
        self.encryptFrame.AccentButton("Encrypt", command=self.tree_encrypt, colspan=2)
        self.encryptFrame.AccentButton("Delete", command=self.tree_delete, col=1, row=1)
        self.encryptFrame.AccentButton("Import", command=self.tree_import, row=1)

        self.systemFrame = self.paneTop.addLabelFrame("System", col=1)
        self.systemFrame.AccentButton("Kembali", self.handleExit, widgetkwargs={"width": 15})

        self.paneBottom = self.panedWindow.addWindow()
        self.paneBottom.Label(f"All Rights Reserved \u00A9 {date.now().year}", size=10, weight="normal")

        self.run()

    def tree_select(self):
        data = [{**self.treeView.item(index), "path": self.treeData[0]["path"], "index": index} for index in
                self.treeView.selection()]

        return None if not data else data

    def tree_encrypt(self):
        data = self.tree_select()
        length = len(data) if data else 0

        if length == 1:
            message = f"Are you sure you want to encrypt `{data[0]['text']}`?"
            confirm = alert.askquestion("System", message)
        elif length > 1:
            message = f"You have selected {length} files. Are you sure you want to encrypt them?"
            confirm = alert.askquestion("System", message)
        else:
            log.write("No file selected")
            alert.showwarning("System", "Please select a file to encrypt!")
            confirm = "no"

        if confirm == "yes":
            for item in data:
                try:
                    filename = item["text"].split(".")[0]
                    text = file.read(item["path"], item["text"], binary=True)
                    key = random_bytes(16)
                    file.write(PATH_KEY, f"{filename}.key.txt", key, binary=True)
                    cipher = aes.new(key, aes.MODE_OCB)
                    ciphertext, tag = cipher.encrypt_and_digest(text)
                    assert len(cipher.nonce) == 15

                    f = file.write(PATH_DECRYPT, f"{filename}.enc", close=False, binary=True)
                    f.write(tag)
                    f.write(cipher.nonce)
                    f.write(ciphertext)
                    f.write(key)
                    f.close()

                except Exception as e:
                    log.write(f"Error encrypting file `{item['text']}`: {e}")
                    alert.showerror("System", f"An error occurred while encrypting `{item['text']}`: {e}")

            alert.showinfo("System", "File encryption completed successfully.")

    def tree_import(self):
        try:
            filename = self.getfile()
            self.treeView.insert("", "end", text=filename, values=[file.timestamp(PATH_ENCRYPT, filename)])
            alert.showinfo("System", f"File `{filename}` successfully added to tree view.")
        except Exception as e:
            log.write(f"Error importing file: {e}")
            alert.showerror("System", f"An error occurred while importing the file: {e}")

    def tree_delete(self):
        data = self.tree_select()
        length = len(data) if data else 0

        if length == 1:
            message = f"Are you sure you want to delete `{data[0]['text']}`?"
            confirm = alert.askquestion("System", message)
        elif length > 1:
            message = f"You have selected {length} files. Are you sure you want to delete them?"
            confirm = alert.askquestion("System", message)
        else:
            log.write("No file selected")
            alert.showwarning("System", "Please select a file to delete!")
            confirm = "no"

        if confirm == "yes":
            for item in data:
                try:
                    file.delete(item["path"], item["text"])
                    self.treeView.delete(item["index"])
                except Exception as e:
                    log.write(f"Error deleting file `{item['text']}`: {e}")
                    alert.showerror("System", f"An error occurred while deleting `{item['text']}`: {e}")

            alert.showinfo("System", "File deletion completed successfully.")
