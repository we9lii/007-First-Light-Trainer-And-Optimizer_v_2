#!/usr/bin/env python3
"""
007 First Light Trainer & Optimizer – Main Entry Point
"""

import sys
import time
import threading
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from core.trainer_engine import TrainerEngine
from core.feature_manager import FeatureManager
from utils.logger import setup_logger, log_info, log_success, log_error
from utils.config_loader import load_config
from utils.hotkey_manager import HotkeyManager
from gui.console_renderer import ConsoleRenderer

def main():
    config = load_config("config.ini")
    log_info("007 First Light Trainer v1.0 starting...")
    
    engine = TrainerEngine()
    feature_mgr = FeatureManager()
    hotkey_mgr = HotkeyManager()
    renderer = ConsoleRenderer()
    
    hotkey_mgr.register_hotkey('f1', lambda: renderer.toggle_menu())
    hotkey_mgr.register_hotkey('f2', lambda: feature_mgr.toggle('godmode'))
    hotkey_mgr.register_hotkey('f3', lambda: feature_mgr.toggle('infinite_ammo'))
    hotkey_mgr.register_hotkey('f4', lambda: feature_mgr.toggle('stealth'))
    hotkey_mgr.register_hotkey('f5', lambda: feature_mgr.trigger('unlock_gadgets'))
    hotkey_mgr.register_hotkey('f6', lambda: feature_mgr.trigger('unlock_outfits'))
    hotkey_mgr.register_hotkey('f7', lambda: feature_mgr.trigger('reveal_intel'))
    hotkey_mgr.register_hotkey('f8', lambda: feature_mgr.trigger('optimize_fps'))
    hotkey_mgr.register_hotkey('f9', lambda: sys.exit(0))
    
    engine_thread = threading.Thread(target=engine.run, args=(feature_mgr,), daemon=True)
    engine_thread.start()
    
    log_success("Trainer ready. Press F1 for help, F9 to exit.")
    
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        log_info("Shutting down...")
        sys.exit(0)

if __name__ == "__main__":
    main()
