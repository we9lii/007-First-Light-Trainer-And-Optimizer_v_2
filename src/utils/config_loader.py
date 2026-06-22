import configparser
import os

def load_config(filename="config.ini"):
    config = configparser.ConfigParser()
    if os.path.exists(filename):
        config.read(filename)
    else:
        config["Settings"] = {
            "godmode_key": "f2",
            "ammo_key": "f3",
            "stealth_key": "f4",
            "gadgets_key": "f5",
            "outfits_key": "f6",
            "intel_key": "f7",
            "fps_key": "f8",
            "exit_key": "f9"
        }
        with open(filename, "w") as f:
            config.write(f)
    return config["Settings"]
