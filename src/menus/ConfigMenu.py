import os
from InquirerPy import inquirer
from rich.text import Text
from src.utils import console
from src.menus.InstallDependencies import InstallDependencies

class ConfigMenu:
    def __init__(self, version: str, user_selects: dict):
        self.version = version
        self.user_selects = user_selects

    def _render_header(self):
        console.print(
            "Configuração das Variáveis de Ambiente.\n"
            "Preencha os campos abaixo para configurar seu bot.\n",
            style="white",
        )

    def show(self):
        self._render_header()

        bot_token = inquirer.secret(
            message="🤖 Digite o Token do seu bot do Discord:",
            validate=lambda v: True if any(c.isalpha() for c in v) else "O token precisa conter pelo menos UMA letra!",
        ).execute()

        square_token = inquirer.secret(
            message="☁️ Digite a sua API KEY da Square Cloud:",
            validate=lambda v: True if any(c.isalpha() for c in v) else "A API KEY precisa conter pelo menos UMA letra!",
        ).execute()

        app_id = inquirer.text(
            message="🆔 Digite o ID da sua aplicação do Discord:",
            validate=lambda v: True if v.isdigit() and len(v) >= 2 else "O ID deve conter APENAS números e ter pelo menos 2 dígitos!",
        ).execute()

        self.user_selects.update({
            "BOT_TOKEN": bot_token,
            "SQUARE_CLOUD_TOKEN": square_token,
            "APPLICATION_ID": app_id
        })

        return self._handle_config_success()

    def _handle_config_success(self):
        console.clear()
        console.print(f"[bold green]✔[/bold green] [white]Configurações salvas com sucesso![/white]")
        
        new_menu = InstallDependencies(self.version, self.user_selects)
        new_menu.show()
        
        return self.user_selects