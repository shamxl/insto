from typer import Typer
from rich import print
from .login import login_to_instagram
from insto.logger import info
app = Typer()

@app.command()
def login (session_id: str) -> None:
    info ("logging in with session id...")
    login_to_instagram(session_id)