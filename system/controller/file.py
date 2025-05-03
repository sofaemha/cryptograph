from system.py.core import os


class File:

    @staticmethod
    def read(directory, file_name, binary=False):
        # Read the contents of a file and return it as a string.
        if binary:
            with open(f"{directory}{file_name}", "rb") as file:
                print(file.read())
                file.close()
        else:
            with open(f"{directory}{file_name}", "r") as file:
                print(file.read())
                file.close()

    @staticmethod
    def write(directory, file_name, content, binary=False):
        # Write the contents of a string to a file.
        if binary:
            with open(f"{directory}{file_name}", "wb") as f:
                f.write(content)
                f.close()
        else:
            with open(f"{directory}{file_name}", "w") as f:
                f.write(content)
                f.close()

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


file = File()
