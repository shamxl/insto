from instagrapi import Client
from rich import print

def login_to_instagram (username: str, password: str) -> bool:
    cl = Client()
    try:
        cl.login(username, password)

        user_id = cl.user_id_from_username(username)
        print(f"User id: {user_id}")
    except Exception:
        print ("[bold red]Login failed.[/bold red]")
        return False
    return True