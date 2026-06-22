from colorama import init, Fore, Style
init(autoreset=True)

def setup_logger():
    pass

def log_info(msg):
    print(f"{Fore.CYAN}[INFO] {msg}")

def log_success(msg):
    print(f"{Fore.GREEN}[SUCCESS] {msg}")

def log_warning(msg):
    print(f"{Fore.YELLOW}[WARN] {msg}")

def log_error(msg):
    print(f"{Fore.RED}[ERROR] {msg}")

def log_debug(msg):
    print(f"{Fore.BLUE}[DEBUG] {msg}")
