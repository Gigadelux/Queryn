import logging
import shutil
import subprocess
from pathlib import Path

import PyInstaller.__main__
from colorama import Fore, Style, init

init()
logging.basicConfig(format="%(message)s")
logger = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parent
# queryn-serve and queryn-app are sibling apps under app/; the compiled
# binary is picked up by Tauri as a sidecar from queryn-app/src-tauri/binaries.
BINARIES_DIR = (ROOT / ".." / "queryn-app" / "src-tauri" / "binaries").resolve()


def colored_log(message, color=Fore.WHITE):
    logger.info(f"{color}{message}{Style.RESET_ALL}")


def install():
    colored_log("Building FastAPI Binary...", Fore.CYAN)
    path_to_main = str(ROOT / "main.py")
    try:
        PyInstaller.__main__.run(
            [path_to_main, "--onefile", "--name=api", "--log-level=ERROR"]
        )
    except Exception as e:
        colored_log(f"Error during PyInstaller build: {e}", Fore.RED)
        return
    post_install()


def post_install() -> None:
    colored_log("Running post-build steps...", Fore.CYAN)
    BINARIES_DIR.mkdir(parents=True, exist_ok=True)

    try:
        rustc_output = subprocess.check_output(
            ["rustc", "-Vv"], universal_newlines=True
        )
        host_info = next(
            (
                line.split(": ")[1].strip()
                for line in rustc_output.split("\n")
                if line.startswith("host:")
            ),
            "",
        )
        colored_log(f"Rust host info: {host_info}", Fore.GREEN)
    except (subprocess.CalledProcessError, FileNotFoundError):
        host_info = "unknown-host"
        colored_log("Warning: Failed to get rustc host information", Fore.YELLOW)

    colored_log("Moving files to queryn-app/src-tauri/binaries...", Fore.CYAN)
    source = ROOT / "dist"

    # Dynamically handles the .exe suffix for Windows
    file_suffix = ".exe" if (source / "api.exe").exists() else ""
    source_file = source / f"api{file_suffix}"
    destination_file = BINARIES_DIR / f"api-{host_info}{file_suffix}"

    if source_file.exists():
        try:
            shutil.move(str(source_file), str(destination_file))
            colored_log(f"Updated {destination_file.name}", Fore.GREEN)
        except Exception as e:
            colored_log(f"Error moving {source_file}: {e}", Fore.RED)
    else:
        colored_log(f"File not found: {source_file}", Fore.RED)

    colored_log("Cleaning up temporary files...", Fore.CYAN)
    cleanup_paths = [ROOT / "dist", ROOT / "build", ROOT / "api.spec"]
    for path in cleanup_paths:
        if path.exists():
            try:
                if path.is_dir():
                    shutil.rmtree(path)
                else:
                    path.unlink()
                colored_log(f"Removed {path.name}", Fore.GREEN)
            except Exception as e:
                colored_log(f"Error removing {path}: {e}", Fore.RED)


if __name__ == "__main__":
    install()
