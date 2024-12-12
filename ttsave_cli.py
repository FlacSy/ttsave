import os
import yaml
import requests
import click
from click_shell import shell
from rich.console import Console
from colorama import Fore
from ttsave import TTSave

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

def load_config():
    config_path = "ttsave_cli_config.yml"
    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    return {}

def save_config(config):
    config_path = "ttsave_cli_config.yml"
    with open(config_path, 'w') as file:
        yaml.dump(config, file)

config = load_config()

@shell(prompt=Fore.RESET+'TTSave >  ', intro=intro)
def cli():
    """Main CLI function"""
    pass

@cli.command()
@click.argument('url')
@click.argument('download_dir', required=False)
@click.argument('tt_chain_token', required=False)
# @click.option('--debug', is_flag=True, help="Enable debug mode.")
def download(url, tt_chain_token, download_dir):
    
    if download_dir is None:
        download_dir = config.get('default', {}).get('download_dir', os.getcwd())
        
    if tt_chain_token is None:
        tt_chain_token = config.get('default', {}).get('tt_chain_token', None)
        if tt_chain_token is None:
            console.print("Please provide a tt_chain_token.", style="bold red")
            return
        
    if not os.path.exists(download_dir):
        console.print(f"Directory does not exist: {download_dir}", style="bold red")
        return
  
    ttsave = TTSave(download_dir, tt_chain_token)

    try:
        url = requests.get(url).url
        result = ttsave.save(url)
        config['default'] = {'download_dir': download_dir, 'tt_chain_token': tt_chain_token}
        save_config(config)
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
    console.print("TTSave CLI version 2.0.0", style="bold cyan")

@cli.command()
def help():
    """Show help information."""
    console.print("Available commands:", style="bold blue")
    console.print(" - [bold cyan]download[/bold cyan]: Download TikTok video or photo")
    console.print(" - [bold cyan]version[/bold cyan]: Show version information")

if __name__ == "__main__":
    cli()