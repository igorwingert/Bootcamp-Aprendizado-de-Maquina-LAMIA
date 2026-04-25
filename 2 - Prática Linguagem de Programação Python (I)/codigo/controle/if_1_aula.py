nota = float(input('Informe a nota do aluno: '))
# adiciona a verificação de comportamento
comportado = True if input('Comportado (s/n): ') == 's' else False

if nota >= 9 and comportado:
    print('Duas palavras: para béns :D')  # não tem muito o que explicar
    print('Quadro de Honra')
elif nota >= 7:
    print('Aprovado')
elif nota >= 5.5:
    print('Recuperaçao!')
elif nota >= 3.5:
    print('Recuperação + Trabalho')
else:
    print('Reprovado!!!!!!')

print(nota)
