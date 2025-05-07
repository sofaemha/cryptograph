from system.py.core import os, date


class File:

    @staticmethod
    def read(directory, file_name, close=True, binary=False):
        # Read the contents of a file and return it as a string.
        if close:
            if binary:
                with open(f"{directory}{file_name}", "rb") as f:
                    content = f.read()
                    print(content)
                    f.close()
                    return content
            else:
                with open(f"{directory}{file_name}", "r") as f:
                    content = f.read()
                    print(content)
                    f.close()
                    return content
        else:
            if binary:
                f = open(f"{directory}{file_name}", "rb")
                return f
            else:
                f = open(f"{directory}{file_name}", "r")
                return f

    @staticmethod
    def write(directory, file_name, content=None, close=True, binary=False):
        # Write the contents of a string to a file.
        if close:
            if binary:
                with open(f"{directory}{file_name}", "wb") as f:
                    f.write(content)
                    f.close()
            else:
                with open(f"{directory}{file_name}", "w") as f:
                    f.write(content)
                    f.close()
        else:
            if binary:
                f = open(f"{directory}{file_name}", "wb")
                return f
            else:
                f = open(f"{directory}{file_name}", "w")
                return f

    @staticmethod
    def append(directory, file_name, content, binary=False):
        # Append the contents of a string to a file.
        if binary:
            with open(f"{directory}{file_name}", "ab") as f:
                f.write(content)
                f.close()
        else:
            with open(f"{directory}{file_name}", "a") as f:
                f.write(content)
                f.close()

    @staticmethod
    def check(directory, file_name):
        # Check if a file exists.
        return os.path.isfile(f"{directory}{file_name}")

    @staticmethod
    def delete(directory, file_name):
        # Delete a file.
        try:
            os.remove(f"{directory}{file_name}")
            print(f"File `{file_name}` in `{directory} was deleted.")
        except FileNotFoundError:
            print(f"File `{file_name}` not found in `{directory}`.")

    @staticmethod
    def timestamp(directory, file_name):
        # Get the last modified time of a file.
        return date.fromtimestamp(os.path.getmtime(f"{directory}{file_name}")).strftime(
            "%Y-%m-%d %H:%M:%S") if os.path.exists(directory) else None


file = File()
