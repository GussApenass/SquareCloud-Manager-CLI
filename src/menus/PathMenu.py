import os
from InquirerPy import inquirer
from InquirerPy.validator import PathValidator
from .ConfigMenu import ConfigMenu
from src.utils import console

class PathMenu:
    def __init__(self, version: str):
        self.version = version

    def show(self):
        path = inquirer.filepath(
            message="📁 Onde a pasta do Square Cloud Manager será criada?",
            default="./",
            validate=PathValidator(is_dir=True, message="Essa pasta não existe! Tente novamente."),
            only_directories=True,
            instruction="(TAB para autocompletar)"
        ).execute()

        return self._handle_path_success(path)

    def _handle_path_success(self, path):
        absolute_path = os.path.abspath(path)

        user_selects = {
            "path": absolute_path
        }

        console.print(f"[bold green]✔[/bold green] [white]Caminho validado:[/white] [cyan]{absolute_path}[/cyan]\n")
        new_menu = ConfigMenu(self.version, user_selects)
        new_menu.show()
        
        return absolute_path