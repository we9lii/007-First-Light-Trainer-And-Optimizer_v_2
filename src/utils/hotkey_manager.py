import keyboard
from utils.logger import log_info

class HotkeyManager:
    def __init__(self):
        self.hotkeys = {}
    
    def register_hotkey(self, key, callback):
        keyboard.add_hotkey(key, callback)
        log_info(f"Registered hotkey: {key}")
    
    def unregister_all(self):
        keyboard.unhook_all()
