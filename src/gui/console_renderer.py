from utils.logger import log_info

class ConsoleRenderer:
    def __init__(self):
        self.menu_visible = False
    
    def toggle_menu(self):
        self.menu_visible = not self.menu_visible
        if self.menu_visible:
            self.show_menu()
        else:
            log_info("Menu hidden")
    
    def show_menu(self):
        print("""
╔══════════════════════════════════════╗
║   🔫 007 FIRST LIGHT TRAINER v1.0   ║
║   🔥 F2 - God Mode                  ║
║   🔥 F3 - Infinite Ammo             ║
║   🔥 F4 - Stealth Mode              ║
║   🔥 F5 - Unlock All Gadgets        ║
║   🔥 F6 - Unlock All Outfits        ║
║   🔥 F7 - Reveal Map Intel          ║
║   🔥 F8 - FPS Optimizer (FOV/DLSS)  ║
║   🔥 F9 - Exit                      ║
╚══════════════════════════════════════╝
        """)
