from system.controller.file import file
from system.py.core import env


PY_THEME = env("PY_THEME")
PY_MODE = file.theme("get")


class Route:
    def __init__(self):
        self.options = {"theme": PY_THEME, "mode": PY_MODE}

    def root(self):
        import view.app.root as root
        return root.App(**self.options)


route = Route()
