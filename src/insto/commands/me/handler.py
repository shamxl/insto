import typer
from insto.utils import get_client
from insto.logger import info

app = typer.Typer()

@app.command()
def me ():
    client = get_client()
    account_info = client.account_info()
    info(f"logged in as: [white]{account_info.username}[/white]")