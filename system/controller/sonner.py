class Sonner:
    @staticmethod
    def write(message, title="INFO", flag="system"):
        print(f"[{flag}] {title}: {message}\n")

    def ubuntu_library(self):
        flag = "ubuntu"
        self.write("sudo add-apt-repository universe", "FUSE", flag)
        self.write("sudo apt install libfuse2", "FUSE", flag)
        self.write("sudo apt-get install python3-tk", "Tkinter", flag)


sonner = Sonner()
