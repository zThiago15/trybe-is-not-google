"""module sys to provide the file object 'sys.stderr' when there's an error
and os to manipulate path"""
import sys
import os


def txt_importer(path_file):
    """Validate and read a txt file"""
    _, ext = os.path.splitext(path_file)
    if ext != '.txt':
        print('Formato inválido', file=sys.stderr)
        return []

    if not os.path.exists(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return []

    with open(path_file, "r", encoding="utf-8") as file:
        return file.read().split('\n')
