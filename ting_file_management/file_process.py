import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue

def process(path_file: str, instance: Queue):
    """Aqui irá sua implementação"""
    for index in range(len(instance)):
        file = instance.search(index)
        if file["nome_do_arquivo"] == path_file:
            return False

    content = txt_importer(path_file)

    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": content,
    }
    print(file_info)


def remove(instance: Queue):
    """Remove first item of queue"""

    if len(instance.items) == 0:
        return sys.stdout.write("Não há elementos\n")

    file_removed = instance.dequeue()
    path_file = file_removed["nome_do_arquivo"]

    return sys.stdout.write(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
