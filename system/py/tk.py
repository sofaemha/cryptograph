from system.py.core import env, fs
import tkinter as tk
import TKinterModernThemes as tkt
from tkinter import filedialog, messagebox as alert

PATH_ENCRYPT = env("PATH_ENCRYPT")
PATH_DECRYPT = env("PATH_DECRYPT")

def getfile(types):
    if types == "txt":
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt")],
            title="Select a Text File",
        )
        return data(file_path, types)
    elif types == "enc":
        file_path = filedialog.askopenfilename(
            filetypes=[("Encrypted Files", "*.enc")],
            title="Select an Encrypted File",
        )
        return data(file_path, types)


def data(path, types):
    files = "a text" if types == "txt" else "an encrypted"
    if path:
        filename = path.split("/")[-1]
        fs.copy(path, PATH_ENCRYPT) if types == "txt" else fs.copy(path, PATH_DECRYPT)
        alert.showinfo("System", f"File `{filename}` successfully imported into `{PATH_ENCRYPT}`.")
        return filename
    else:
        alert.showwarning("System", f"Please select {files} (.{types}) file!")
