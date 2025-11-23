"""
Script to remove TeX auxiliary files
"""

import inspect
import os.path
from pathlib import Path
from typing import Literal


def remove_auxiliary_tex_files() -> None:
    """
    Remove auxiliary files generated during compilation of TeX files
    """
    file_extensions = get_auxiliary_tex_file_extensions()
    root_folder = get_repo_root_folder()

    files_removed = 0

    for directory, _, filenames in os.walk(root_folder):
        excluded_dirs = [".git", ".venv", ".ruff_cache"]
        excluded_dirs_flag = [(e in directory) for e in excluded_dirs]
        if any(excluded_dirs_flag):
            continue
        print(directory)

        for filename in filenames:
            extension_to_exclude = [filename.endswith(e) for e in file_extensions]
            full_file_name = os.path.join(directory, filename)
            if any(extension_to_exclude):
                os.remove(full_file_name)
                files_removed += 1
                print(f'{files_removed} - Removed file "{full_file_name}"')


def get_auxiliary_tex_file_extensions() -> list[str]:
    """
    Get auxiliary TeX file extensions
    """
    file_extensions = ["log"]

    root_folder = get_repo_root_folder()
    os.chdir(root_folder)

    if os.path.exists(".gitignore"):
        with open(".gitignore", mode="r", encoding="utf-8") as file:
            line = file.readline()
            header_found = False

            while line:
                if header_found and len(line) >= 4:
                    stripped_line = line.strip()
                    extension = stripped_line.split(".")[1:]
                    extension = ".".join(extension)
                    file_extensions.append(extension)

                if line.strip() == "# TeX support files":
                    header_found = True
                elif line.startswith("#") and header_found:
                    break

                line = file.readline()
    else:
        raise FileNotFoundError(".gitignore file not found in root folder")

    return file_extensions


def get_repo_root_folder() -> Path | Literal[""]:
    """
    Get root folder of repository
    """
    current_folder = Path(get_current_folder())
    parent = current_folder
    dirnames = os.listdir(current_folder)

    max_levels = 10
    counter = 0

    while ".git" not in dirnames:
        parent = parent.parent
        dirnames = os.listdir(parent)
        counter += 1
        if counter > max_levels:
            break

    if ".git" in dirnames:
        root_folder = parent
    else:
        root_folder = ""

    return root_folder


def get_current_folder() -> str:
    """
    Get current folder where this file is located
    """
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.dirname(os.path.abspath(filename))
    return path


def main() -> None:
    """
    Entry point
    """
    remove_auxiliary_tex_files()


if __name__ == "__main__":
    main()
