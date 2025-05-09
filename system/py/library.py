import json
import importlib.util as library_hook

from system.controller.file import file
from system.controller.sonner import sonner
from system.py.core import system
from system.controller.log import log


class Library:

    def check(self):
        f = file.read('', 'package.json', close=False)
        data = json.loads(f.read())
        f.close()

        module_status = [self.find(name) for name in data["modules"]]

        return all(module_status)

    @staticmethod
    def find(module_name):
        if module_name in system.modules:
            try:
                module_version = system.modules[module_name].__version__
            except AttributeError:
                module_version = "unknown"

            log.write(f"Module {module_name!r} (v-{module_version}) already in `sys.modules`")
            return True
        elif (spec := library_hook.find_spec(module_name)) is not None:
            module = library_hook.module_from_spec(spec)
            try:
                module_version = module.version
                print(module_version)
            except AttributeError:
                module_version = "unknown"

            log.write(f"Module {module_name!r} (v-{module_version}) found")

            try:
                system.modules[module_name] = module
                spec.loader.exec_module(module)
                log.write(f"Module {module_name!r} has been imported")
                return True
            except ImportError as e:
                log.write(f"Module {module_name!r} not found: {e}")
                return False
        else:
            log.write(f"Can't find {module_name!r} module")
            sonner.ubuntu_library()
            return False


library = Library()
