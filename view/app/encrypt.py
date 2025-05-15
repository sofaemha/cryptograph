from system.py.core import date, env
from system.controller.log import log
from system.controller.file import file
from system.py.crypt import crypt
from system.py.tk import tk, tkt, getfile, alert
from system.controller.folder import folder

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
        self.encryptFrame = None
        self.systemFrame = None
        self.paneBottom = None

        self.pane_top()
        self.tree_frame()
        self.encrypt_frame()
        self.system_frame()
        self.pane_bottom()

        self.run()

    def pane_top(self):
        self.paneTop = self.panedWindow.addWindow()
        self.paneTop.Label("AES-FL : Encrypt", colspan=2)

    def pane_bottom(self):
        self.paneBottom = self.panedWindow.addWindow()
        self.paneBottom.Label(f"All Rights Reserved \u00A9 {date.now().year}", size=10, weight="normal")

    def encrypt_frame(self):
        self.encryptFrame = self.paneTop.addLabelFrame("Action", col=1)
        self.encryptFrame.AccentButton("Encrypt", command=self.tree_encrypt, colspan=2)
        self.encryptFrame.AccentButton("Delete", command=self.tree_delete, col=1, row=1)
        self.encryptFrame.AccentButton("Import", command=self.tree_import, row=1)

    def system_frame(self):
        self.systemFrame = self.paneTop.addLabelFrame("System", col=1)
        self.systemFrame.AccentButton("Kembali", self.handleExit, widgetkwargs={"width": 15})

    def tree_frame(self):
        self.treeFrame = self.paneTop.addLabelFrame("Data", rowspan=2)
        self.treeRawFolder = [f'{PATH_ENCRYPT}{filename}' for filename in self.folder.list(PATH_ENCRYPT)]
        self.treeFolder = [
            [f, file.timestamp(f"{"/".join(f.split("/")[:-1])}/", f.split("/")[-1])] for f in self.treeRawFolder
        ]
        self.treeData = [
            {"encrypt": f[0].split("/")[-1], "date": f[1]} for f in self.treeFolder
        ]
        self.treeView = self.treeFrame.Treeview(["Encrypt", "Date"], [150, 150], 5, self.treeData, None,
                                                ["encrypt", "date"])

    def tree_select(self):
        data = [{**self.treeView.item(index), "path": PATH_ENCRYPT, "index": index} for index in
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
            crypt.encrypt(data)
            alert.showinfo("System", "File encryption completed successfully.")

    def tree_import(self):
        try:
            filename = self.getfile("txt")
            if filename:
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
