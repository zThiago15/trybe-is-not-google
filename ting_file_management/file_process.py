import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file: str, instance: Queue):
    """Aqui irá sua implementação"""
    path_file_names = [instance.search(index)['nome_do_arquivo']
                       for index in range(len(instance))]

    if path_file not in path_file_names:
        content = txt_importer(path_file)
        dict_data = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': len(content),
            'linhas_do_arquivo': content,
        }

        instance.enqueue(dict_data)
        print(dict_data, file=sys.stdout)


def remove(instance: Queue):
    """Remove first item of queue"""

    if len(instance.items) == 0:
        return print("Não há elementos", file=sys.stdout)

    file_removed = instance.dequeue()
    path_file = file_removed["nome_do_arquivo"]
    print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance: Queue, position):
    """Aqui irá sua implementação"""
    try:
        dict_search = instance.search(position)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
    else:
        print(dict_search, file=sys.stdout)
