from system.py.core import env, date
from system.control.file import file

folder_public = env("FOLDER_PUBLIC")
file_log = env("FILE_LOG")


class Log:
    # function for generating log with message
    def write(self, message, path=file_log):
        timestamp = date.now().strftime("%d/%m/%Y.%H:%M:%S")
        message = f"[{timestamp}] {message}\n"
        file.append(folder_public, path, message)
        self.last()

    # function for reading log file
    @staticmethod
    def all(path=file_log):
        file.read(folder_public, path)

    # function for py last line in log file
    @staticmethod
    def last(path=file_log):
        with open(f"{folder_public}{path}") as f:
            for line in f:
                pass
            last_line = line
            print(last_line)
            f.close()

    # function for clear log file content
    @staticmethod
    def clear(path=file_log):
        file.write(folder_public, path, "")


log = Log()
