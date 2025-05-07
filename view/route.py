from system.py.core import env

PY_THEME = env("PY_THEME")
PY_MODE = env("PY_MODE")


class Route:
    def __init__(self):
        self.options = {"theme": PY_THEME, "mode": PY_MODE}

    def root(self):
        import view.app.root as root
        return root.App(**self.options)

    def about(self):
        import view.app.about as about
        return about.App(**self.options)


route = Route()
