from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from rich.text import Text
from .PathMenu import PathMenu
from src.utils import console

class InitialMenu:
    def __init__(self, version: str):
        self.version = version

    def _render_header(self):
        title = Text()
        title.append("📦 Square Cloud Manager CLI ", style="bold cyan")
        title.append("| ", style="bold bright_black")
        title.append(f"| v{self.version} ", style="bright_black underline")
        title.append("💎\n", style="bold cyan")

        console.print(title)
        console.print(
            "Bem-vindo(a) ao SCMC (Square Cloud Manager CLI).\n"
            "Aqui, você poderá iniciar o projeto do Square Cloud Manager\n"
            "de forma fácil, rápida e prática.\n",
            style="white",
        )

    def show(self):
        self._render_header()

        choice = inquirer.select(
            message="O que deseja fazer?",
            choices=[
                Choice(value="continue", name="◈ Continuar"),
                Choice(value="exit", name="✕ Exit"),
            ],
            pointer="❯",
            instruction="(↑↓ Navegar • ⏎ Selecionar)"
        ).execute()

        if choice == "continue":
            self._continue()
        elif choice == "exit":
            self._exit()

    def _continue(self):
        new_menu = PathMenu(self.version)
        new_menu.show()

    def _exit(self):
        console.print("\n[red]Saindo...[/red]\n")
        raise SystemExit