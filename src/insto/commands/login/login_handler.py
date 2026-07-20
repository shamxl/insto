from typer import Typer
from rich import print
from .login import login_to_instagram

app = Typer()

@app.command()
def login (username: str, password: str) -> None:
    print (f"[bold]Logging in as[/bold] \'{username}\'")
    login_to_instagram(username, password)