import importlib.util as library_hook

from system.controller.sonner import sonner
from system.py.core import system
from system.controller.log import log
from system.library.pycryptodome import pycryptodome
from system.library.tkinter import tkinter
from system.library.tkintertheme import tkintertheme


class Library:

    def check(self, module, fn):

        module_status = [self.find(name) for name in module]

        for name, status in zip(fn, module_status):
            func = globals().get(name)
            if callable(func):
                func(status)
            else:
                log.write(f"Function {name} not found")
                return False

        return all(module_status)

    @staticmethod
    def find(module_name):
        if module_name in system.modules:
            log.write(f"Module `{module_name!r}` already in `sys.modules`")
            return True
        elif (spec := library_hook.find_spec(module_name)) is not None:
            module = library_hook.module_from_spec(spec)
            system.modules[module_name] = module
            spec.loader.exec_module(module)
            log.write(f"Module {module_name!r} has been imported")
            return True
        else:
            log.write(f"Can't find the `{module_name!r}` module")
            sonner.ubuntu_library()
            return False


library = Library()
