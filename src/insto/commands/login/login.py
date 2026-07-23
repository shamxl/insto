from instagrapi import Client
from rich import print
from insto.utils import get_config_path

def login_to_instagram (session_id: str) -> bool:
    cl = Client()
    try:
        cl.login_by_sessionid(session_id)
    except Exception as e:
        print("[red]Login failed[/red]")
        print ("[red]Reason:[/red]", e)
        return False
    
    settings_path = get_config_path() / "settings.json"
    cl.dump_settings(settings_path)
    username = cl.account_info().username
    print(f"[bold green]Logged in as: {username}[/bold green]")
   
    return True
