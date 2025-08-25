from rich.console import Console

console = Console()
def textColor(color,text):
    console.print("[bold" + color + "]" + text + "[/bold" + color + "]")