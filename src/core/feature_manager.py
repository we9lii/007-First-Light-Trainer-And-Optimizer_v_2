from utils.logger import log_success, log_info

class FeatureManager:
    def __init__(self):
        self.features = {
            "godmode": False,
            "infinite_ammo": False,
            "stealth": False,
        }
        self.unlocked_gadgets = False
        self.unlocked_outfits = False
        self.intel_revealed = False
        self.optimized = False
    
    def toggle(self, name):
        if name in self.features:
            self.features[name] = not self.features[name]
            status = "ON" if self.features[name] else "OFF"
            log_success(f"{name.upper()} {status}")
    
    def trigger(self, name):
        if name == "unlock_gadgets":
            self.unlocked_gadgets = True
            log_success("All gadgets unlocked!")
        elif name == "unlock_outfits":
            self.unlocked_outfits = True
            log_success("All outfits unlocked!")
        elif name == "reveal_intel":
            self.intel_revealed = True
            log_success("Map intel revealed!")
        elif name == "optimize_fps":
            self.optimized = True
            log_success("FPS optimization applied (FOV, DLSS, stutter fix)")
        else:
            log_info(f"Triggered: {name}")
