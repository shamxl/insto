from typer import Typer
from .commands import core_app
from .utils import print_logo
from .commands.login import login_handler

app = Typer()
app.add_typer(core_app)
app.add_typer(login_handler)

def run_app () -> None:
    print_logo()
    app()