import typer
from rich import print
from importlib.metadata import version as ver
app = typer.Typer()

@app.command()
def version () -> None:
    print("[bold green]Insto[/bold green] [bold]version:[/bold]", ver("insto"))