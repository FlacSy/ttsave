import os
import click
from click_shell import shell
from rich.console import Console
from ttsave import TTSave
from selenium import webdriver
from colorama import Fore


console = Console()

intro = Fore.CYAN + r"""
╔═══════════════════════════════════════════════════════════════════════════╗

_______________________________   _________   _______________
\__    ___/\__    ___/   _____/  /  _  \   \ /   /\_   _____/
  |    |     |    |  \_____  \  /  /_\  \   Y   /  |    __)_ 
  |    |     |    |  /        \/    |    \     /   |        \
  |____|     |____| /_______  /\____|__  /\___/   /_______  /
                            \/         \/                 \/ 

╚═══════════════════════════════════════════════════════════════════════════╝
""" + Fore.GREEN +"""
Welcome to TTSave CLI! Type 'help' for commands.
"""

@shell(prompt='TTSave >  ', intro=intro)
def cli():
    """Main CLI function"""
    pass

@cli.command()
@click.argument('url')
@click.argument('download_dir', required=False)
@click.option('--debug', is_flag=True, help="Enable debug mode.")
def download(url, download_dir, debug):
    """Download TikTok video or photo from the given URL."""
    if download_dir is None:
        download_dir = os.getcwd()

    if not os.path.exists(download_dir):
        console.print(f"Directory does not exist: {download_dir}", style="bold red")
        return

    options = webdriver.ChromeOptions()
    ttsave = TTSave(url=url, options=options, download_dir=download_dir, debug_mode=debug, driver_class=webdriver.Chrome)

    try:
        result = ttsave.download()
        if result:
            console.print(f"Downloaded {result['type']} files:", style="bold green")
            for file in result['files']:
                console.print(f" - {file}", style="dim")
        else:
            console.print("No files were downloaded.", style="yellow")
    except Exception as e:
        console.print(f"An error occurred: {e}", style="bold red")

@cli.command()
def version():
    """Show version information."""
    console.print("TTSave CLI version 1.0.0", style="bold cyan")

@cli.command()
def help():
    """Show help information."""
    console.print("Available commands:", style="bold blue")
    console.print(" - [bold cyan]download[/bold cyan]: Download TikTok video or photo")
    console.print(" - [bold cyan]version[/bold cyan]: Show version information")


if __name__ == "__main__":
    cli()
