from functools import reduce

alunos = [
    {'nome': 'Igor', 'nota': 7.2},
    {'nome': 'Wini', 'nota': 8.1},
    {'nome': 'Gabriel', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Maria', 'nota': 6.7},
]


def somar(a, b): return a + b


alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7]
notas_alunos_aprovados = [aluno['nota'] for aluno in alunos_aprovados]
total = reduce(somar, notas_alunos_aprovados, 0)
print(total / len(list(alunos_aprovados)))
