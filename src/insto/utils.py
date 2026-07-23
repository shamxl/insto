from pathlib import Path
from pyfiglet import Figlet 
from rich import print
from instagrapi import Client

def print_logo () -> None:
    f = Figlet (font='slant').renderText("Insto")
    print(f"[bold green]{f}[/bold green]")
    
    
def get_config_path ():
    home = Path.home()
    config_dir = home / ".config/insto/"
    config_dir.mkdir(exist_ok=True, parents=True)
    
    return config_dir

def get_settings (): 
    settings = get_config_path() / "settings.json"
    if settings.exists():
        return settings
    else:
        raise Exception("no login found use `insto login`")
    
def get_client ():
    settings = get_settings()
    cl = Client()
    cl.load_settings(settings)
    
    return cl