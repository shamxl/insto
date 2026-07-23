from pathlib import Path
from pyfiglet import Figlet 
from rich import print

def print_logo () -> None:
    f = Figlet (font='slant').renderText("Insto")
    print(f"[bold green]{f}[/bold green]")
    
    
def get_config_path ():
    home = Path.home()
    config_dir = home / ".config/insto/"
    config_dir.mkdir(exist_ok=True, parents=True)
    
    return config_dir