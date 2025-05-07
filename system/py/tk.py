from system.py.core import env, fs
import tkinter as tk
import TKinterModernThemes as tkt
from tkinter import filedialog, messagebox as alert

PATH_ENCRYPT = env("PATH_ENCRYPT")

def getfile():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")],
        title="Select a Text File",
    )
    if file_path:
        filename = file_path.split("/")[-1]
        fs.copy(file_path, PATH_ENCRYPT)
        alert.showinfo("System", f"File `{filename}` successfully imported into `{PATH_ENCRYPT}`.")
        return filename
    else:
        alert.showwarning("System", "Please select a text (.txt) file!")
