from ting_file_management.priority_queue import PriorityQueue

def test_basic_priority_queueing():
    lista_arquvios = [
        {
            "nome_do_arquivo": "arquivo1",
            "rows_qt": 1,
            "linhas_do_arquivo": 'hahaha'
        },
        {
            "nome_do_arquivo": "arquivo2",
            "rows_qt": 6,
            "linhas_do_arquivo": 'hahaha'
        },
        {
            "nome_do_arquivo": "arquivo3",
            "rows_qt": 3,
            "linhas_do_arquivo": 'hahaha'
        },
        {
            "nome_do_arquivo": "arquivo4",
            "rows_qt": 8,
            "linhas_do_arquivo": 'hahaha'
        },
        {
            "nome_do_arquivo": "arquivo5",
            "rows_qt": 2,
            "linhas_do_arquivo": 'hahaha'
        },
    ]
    project_priority = PriorityQueue()

    for indexar in lista_arquvios:
        project_priority.enqueue(indexar)

    assert len(project_priority) == 5
    assert project_priority.search(0)["rows_qt"] == 1
    project_priority.dequeue()
    assert project_priority.search(0)["rows_qt"] == 3
    project_priority.dequeue()
    assert project_priority.search(0)["rows_qt"] == 2
    project_priority.dequeue()
    assert project_priority.search(0)["rows_qt"] == 6
    project_priority.dequeue()
    assert project_priority.search(0)["rows_qt"] == 8
