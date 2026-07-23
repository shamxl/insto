from typer import Typer
from rich import print
from .login import login_to_instagram

app = Typer()

@app.command()
def login (session_id: str) -> None:
    print (f"[bold yellow]logging in with session id...[/bold yellow]")
    login_to_instagram(session_id)