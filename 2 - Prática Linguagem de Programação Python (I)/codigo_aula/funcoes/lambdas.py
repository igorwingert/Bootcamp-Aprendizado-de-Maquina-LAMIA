from functools import reduce

alunos = [
    {'nome': 'Igor', 'nota': 7.2},
    {'nome': 'Wini', 'nota': 8.1},
    {'nome': 'Gabriel', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Maria', 'nota': 6.7},
]


def aluno_aprovado(aluno): return aluno['nota'] >= 7

# def aluno_honra(aluno): return aluno['nota'] >= 9


def obter_nota(aluno): return aluno['nota']


def somar(a, b): return a + b


alunos_aprovados = list(filter(aluno_aprovado, alunos))
notas_alunos_aprovados = list(map(obter_nota, alunos_aprovados))
total = reduce(somar, notas_alunos_aprovados, 0)

print(total / len(list(alunos_aprovados)))
