from instagrapi import Client
from rich import print
from insto.utils import get_config_path
from insto.logger import info, error
def login_to_instagram (session_id: str) -> bool:
    cl = Client()
    try:
        cl.login_by_sessionid(session_id)
    except Exception as e:
        error(e)
        return False
    
    settings_path = get_config_path() / "settings.json"
    cl.dump_settings(settings_path)
    username = cl.account_info().username
    info(f"Logged in as: {username}")
   
    return True
