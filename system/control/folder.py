from system.py.core import os, fs
from system.control.log import log


class Folder:

    def list(self, directory):
        # List all files and directories in a given directory.
        try:
            items = os.listdir(directory)
            log.write(f"Directory `{directory}` contains: {items}")
            return items
        except FileNotFoundError:
            log.write(f"Directory `{directory}` not found.")
            return []

    def delete(self, directory):
        # Delete a directory and all its contents.
        try:
            if os.path.exists(directory):
                fs.rmtree(directory)
                log.write(f"Directory `{directory}` deleted.")
            else:
                log.write(f"Directory `{directory}` does not exist.")
        except Exception as e:
            log.write(f"Error deleting directory `{directory}`: {e}")

    def check(self, directory):
        # Check if a directory exists, and create it if it doesn't.
        try:
            if not os.path.exists(directory):
                log.write(f"Directory `{directory}` does not exist.")
                return False
            else:
                log.write(f"Directory `{directory}` already exists.")
                return True
        except Exception as e:
            log.write(f"Error checking directory `{directory}`: {e}")
            return None

    def create(self, directory):
        # Create a directory if it doesn't exist.
        try:
            if not self.check(directory):
                os.makedirs(directory)
                log.write(f"Directory `{directory}` created.")
        except Exception as e:
            log.write(f"Error creating directory `{directory}`: {e}")


folder = Folder()
