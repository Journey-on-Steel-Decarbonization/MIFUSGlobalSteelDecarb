"""
Script to move all PDF files, generated from TeX folders to PDFs
"""

import inspect
import os.path
from pathlib import Path
from typing import Literal


def get_all_pdfs_generated_from_tex_files(tex_top_folder) -> list[str]:
    """
    Get a list with all PDF files generated from TeX files
    """
    pdf_list: list[str] = []
    for directory, _, filenames in os.walk(tex_top_folder):
        excluded_dirs = [".git", ".venv", ".ruff_cache"]
        excluded_dirs_flag = [(e in directory) for e in excluded_dirs]
        if any(excluded_dirs_flag):
            continue

        for filename in filenames:
            name, extension = os.path.splitext(filename)
            extension = str(extension)

            if extension.lower() == ".pdf":
                print(name, extension)
                full_path = os.path.join(directory, filename)
                pdf_list.append((filename, full_path))

    return pdf_list


def move_pdfs_to_PDF_folder(file_list):
    root_folder = get_repo_root_folder()

    pdf_folder = os.path.join(root_folder, "PDFs")

    for file in file_list:
        new_file_path = os.path.join(pdf_folder, file[0])
        os.replace(file[1], new_file_path)
        print(file[1])


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
    root_folder = get_repo_root_folder()
    tex_top_folder = os.path.join(root_folder, "ZIPs")
    pdfs = get_all_pdfs_generated_from_tex_files(tex_top_folder)
    print(pdfs)
    move_pdfs_to_PDF_folder(pdfs)


if __name__ == "__main__":
    main()
