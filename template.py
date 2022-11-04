import logging
import os
from pathlib import Path


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s %(levelname)s]: %(message)s",
)

while True:
    project_name = input("Enter the project name: ")
    if project_name:
        break

logging.log(logging.INFO, f"Creating project by name {project_name}")

# list of files
list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini",
]


for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)
    if file_dir:
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory at: {file_dir} for file: {file_name}")
    if (not os.path.exists(file_path)) or (not os.path.getsize(file_path)):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Creating a new file: {file_name} at path: {file_path}")
    else:
        logging.info(f"file already exists at: {file_path}")