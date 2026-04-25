pessoas = ['Gui', 'Rebeca']
adj = ['Sapeca', 'Inteligente']

for p in pessoas:  # duplo for (pai e filho)
    for a in adj:
        print(f'{p} é {a}')

for i in [1, 2, 3]:
    pass

for i in range(1, 11):
    if i % 2 == 1:
        continue  # pula iteração
    print(i)

for i in range(1, 11):
    if i == 5:
        break  # para loop, condição de parada
    print(i)

print('Fim!')
