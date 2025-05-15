from system.py.core import date, env
from system.controller.log import log
from system.controller.file import file
from system.py.tk import tk, tkt, getfile, alert
from system.controller.folder import folder
from system.py.crypt import crypt

PATH_ENCRYPT = env("PATH_ENCRYPT")
PATH_DECRYPT = env("PATH_DECRYPT")


class App(tkt.ThemedTKinterFrame):
    def __init__(self, theme, mode, usecommandlineargs=True, usethemeconfigfile=True):
        super().__init__(
            "AES File Locker",
            theme,
            mode,
            usecommandlineargs=usecommandlineargs,
            useconfigfile=usethemeconfigfile,
        )
        self.panedWindow = self.PanedWindow("Decrypt")
        self.root.resizable(False, False)
        self.usecommandargs = tk.BooleanVar(value=True)
        self.usethemeconfigfile = tk.BooleanVar(value=True)
        self.folder = folder
        self.getfile = getfile

        self.paneTop = None
        self.treeFrame = None
        self.treeRawFolder = None
        self.treeFolder = None
        self.treeData = None
        self.treeView = None
        self.decryptFrame = None
        self.systemFrame = None
        self.paneBottom = None

        self.pane_top()
        self.tree_frame()
        self.decrypt_frame()
        self.system_frame()
        self.pane_bottom()

        self.run()

    def pane_top(self):
        self.paneTop = self.panedWindow.addWindow()
        self.paneTop.Label("AES-FL : Decrypt", colspan=2)

    def pane_bottom(self):
        self.paneBottom = self.panedWindow.addWindow()
        self.paneBottom.Label(f"All Rights Reserved \u00A9 {date.now().year}", size=10, weight="normal")

    def decrypt_frame(self):
        self.decryptFrame = self.paneTop.addLabelFrame("Action", col=1)
        self.decryptFrame.AccentButton("Decrypt", command=self.tree_decrypt, colspan=2)
        self.decryptFrame.AccentButton("Delete", command=self.tree_delete, col=1, row=1)
        self.decryptFrame.AccentButton("Import", command=self.tree_import, row=1)

    def system_frame(self):
        self.systemFrame = self.paneTop.addLabelFrame("System", col=1)
        self.systemFrame.AccentButton("Kembali", self.handleExit, widgetkwargs={"width": 15})

    def tree_frame(self):
        self.treeFrame = self.paneTop.addLabelFrame("Data", rowspan=2)
        self.treeRawFolder = [f'{PATH_DECRYPT}{filename}' for filename in self.folder.list(PATH_DECRYPT)]
        self.treeFolder = [
            [f, file.timestamp(f"{"/".join(f.split("/")[:-1])}/", f.split("/")[-1])] for f in self.treeRawFolder
        ]
        self.treeData = [
            {"path": PATH_DECRYPT, "decrypt": f[0].split("/")[-1], "date": f[1]} for f in self.treeFolder
        ]
        self.treeView = self.treeFrame.Treeview(["Decrypt", "Date"], [120, 120], 5, self.treeData, None,
                                                ["decrypt", "date"])

    def tree_select(self):
        data = [{**self.treeView.item(index), "path": PATH_DECRYPT, "index": index} for index in
                self.treeView.selection()]

        return None if not data else data

    def tree_decrypt(self):
        data = self.tree_select()
        length = len(data) if data else 0

        if length == 1:
            message = f"Are you sure you want to decrypt `{data[0]['text']}`?"
            confirm = alert.askquestion("System", message)
        elif length > 1:
            message = f"You have selected {length} files. Are you sure you want to decrypt them?"
            confirm = alert.askquestion("System", message)
        else:
            log.write("No file selected")
            alert.showwarning("System", "Please select a file to decrypt!")
            confirm = "no"

        if confirm == "yes":
            crypt.decrypt(data)
            alert.showinfo("System", "File decryption completed successfully.")

    def tree_import(self):
        try:
            filename = self.getfile("enc")
            if filename:
                self.treeView.insert("", "end", text=filename, values=[file.timestamp(PATH_DECRYPT, filename)])
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
