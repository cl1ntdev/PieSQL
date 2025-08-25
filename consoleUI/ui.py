from rich.console import Console

console = Console()
def txtColor(color,text):
    # console.print("[bold" + color + "]" + text + "[/bold" + color + "]")
    return "[bold " + color +"]" + text + "[/bold " + color + "]"