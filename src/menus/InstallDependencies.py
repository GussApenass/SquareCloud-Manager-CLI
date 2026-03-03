import os
from InquirerPy import inquirer
from src.funcs import SetupManager

class InstallDependencies:
    def __init__(self, version: str, user_selects: dict):
        self.version = version
        self.user_selects = user_selects

    def show(self):
        should_install = inquirer.confirm(
            message="📦 Deseja instalar as dependências (requirements.txt) automaticamente?",
            default=True,
            confirm_letter="s",
            reject_letter="n",
            instruction="(s/n)"
        ).execute()

        return self._start_installation(should_install)

    def _start_installation(self, download_deps: bool):
        setup = SetupManager(self.user_selects)
        setup.install_project(download_dependencies=download_deps)
        
        return True