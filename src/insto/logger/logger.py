from rich import print

def info (txt) -> None:
    print (f"[bold][[/bold][green]INF[/green][bold]][/bold] - [bold green]{txt}[/bold green]")
    
def warn (txt) -> None:
    print (f"[bold][[/bold][yellow]WRN[/yellow][bold]][/bold] - [bold yellow]{txt}[/bold yellow]")
    
def error (err) -> None:
    print (f"[bold][[/bold][red]ERR[/red][bold]][/bold] - [bold red]{err}[/bold red]")
    
    