import subprocess
from version_manager import update_version, update_version_py


def build_executable():
    new_version = update_version()
    update_version_py(new_version)

    subprocess.run([
        "pyinstaller",
        "--name=VoiceScribe11",
        "--windowed",
        "--icon=assets/VoiceScribe11.ico",
        "--add-data", ".env:.",
        "--add-data", "utils/config.ini:.",
        "--add-data", "service/replacements.txt:.",
        "main.py"
    ])

    print(f"Executable built successfully. Version: {new_version}")


if __name__ == "__main__":
    build_executable()
