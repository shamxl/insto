import typer
from insto.utils import get_client
from rich import print

app = typer.Typer()

@app.command()
def me ():
    client = get_client()
    username = get_client().account_info().username
    print (f"logged in as: {username}")