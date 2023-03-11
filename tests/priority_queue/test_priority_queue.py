from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    """Aqui irá sua implementação"""
    pq = PriorityQueue()
    pq.enqueue({"nome": "arquivo1", "qtd_linhas": 3})
    assert len(pq.high_priority) == 1
    assert len(pq.regular_priority) == 0

    # Teste de enfileiramento de arquivo com mais de 5 linhas
    pq.enqueue({"nome": "arquivo2", "qtd_linhas": 7})
    assert len(pq.high_priority) == 1
    assert len(pq.regular_priority) == 1

    # Teste de dequeue com arquivo de alta prioridade
    arquivo_prioritario = pq.dequeue()
    assert arquivo_prioritario["nome"] == "arquivo1"

    # Teste de dequeue sem arquivo de alta prioridade
    arquivo_normal = pq.dequeue()
    assert arquivo_normal["nome"] == "arquivo2"

    # Teste de busca por arquivo em alta prioridade
    pq.enqueue({"nome": "arquivo3", "qtd_linhas": 2})
    assert pq.search(0)["nome"] == "arquivo3"

    # Teste de busca por arquivo em fila regular
    pq.enqueue({"nome": "arquivo4", "qtd_linhas": 8})
    assert pq.search(1)["nome"] == "arquivo4"
