import sys
import logging
import importlib
from pathlib import Path

def load_plugins(plugin_name):
    path = Path(f"Flash/Telethon/{plugin_name}.py")
    name = "Flash.Telethon.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["Spider-Man.Telethon." + plugin_name] = load
    print("Spider Man has Imported " + plugin_name)
