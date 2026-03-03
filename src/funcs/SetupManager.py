import os
import io
import zipfile
import requests
import subprocess
from src.utils import console

class SetupManager:
    def __init__(self, user_selects: dict):
        self.user_selects = user_selects
        self.repo_url = "https://github.com/GussApenass/SquareCloud-Manager/archive/refs/heads/main.zip"
        self.target_path = self.user_selects.get("path")

    def install_project(self, download_dependencies: bool = True):
        try:
            console.print(f"[bold blue]Step 1:[/bold blue] Baixando arquivos do repositório...")
            response = requests.get(self.repo_url)
            response.raise_for_status()

            console.print(f"[bold blue]Step 2:[/bold blue] Extraindo arquivos em [cyan]{self.target_path}[/cyan]...")
            with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
                zip_ref.extractall(self.target_path)
                
                extracted_folder = os.path.join(self.target_path, "SquareCloud-Manager-main")
                for item in os.listdir(extracted_folder):
                    s = os.path.join(extracted_folder, item)
                    d = os.path.join(self.target_path, item)
                    os.rename(s, d)
                os.rmdir(extracted_folder)

            self._create_env_file()

            if download_dependencies:
                self._install_requirements()

            console.print(f"\n[bold green]Projeto configurado com sucesso em:[/bold green] {self.target_path}")

        except Exception as e:
            console.print(f"[bold red]Erro durante a instalação:[/bold red] {e}")

    def _create_env_file(self):
        console.print(f"[bold blue]Step 3:[/bold blue] Gerando arquivo [bold].env[/bold]...")
        env_path = os.path.join(self.target_path, ".env")
        
        env_content = (
            f"BOT_TOKEN={self.user_selects.get('BOT_TOKEN')}\n"
            f"SQUARE_CLOUD_TOKEN={self.user_selects.get('SQUARE_CLOUD_TOKEN')}\n"
            f"APPLICATION_ID={self.user_selects.get('APPLICATION_ID')}\n"
        )
        
        with open(env_path, "w", encoding="utf-8") as f:
            f.write(env_content)
        console.print("[green]✔ .env criado![/green]")

    def _install_requirements(self):
        req_path = os.path.join(self.target_path, "requirements.txt")
        if os.path.exists(req_path):
            console.print(f"[bold blue]Step 4:[/bold blue] Instalando dependências (isso pode demorar)...")
            try:
                subprocess.check_call(["pip", "install", "-r", req_path])
                console.print("[green]✔ Dependências instaladas![/green]")
            except subprocess.CalledProcessError:
                console.print("[yellow]⚠ Falha ao instalar dependências automaticamente. Tente 'pip install -r requirements.txt'.[/yellow]")
        else:
            pass