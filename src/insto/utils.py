from pyfiglet import Figlet 
from rich import print
def print_logo () -> None:
    f = Figlet (font='slant').renderText("Insto")
    print(f"[bold green]{f}[/bold green]")