for i in range(10):
    print(i, end=' ')  # 0 a 9

print('')

for i in range(1, 11):
    print(i, end=' ')  # 1 a 10

print('')

for i in range(1, 100, 7):
    print(i, end=' ')  # 1 somando 7 até 100

print('')

for i in range(20, 0, -3):  # 20 - 3
    print(i, end=' ')

print('')

nums = [2, 4, 6, 8]
for n in nums:
    print(n, end=' ')  # percorre a list


texto = 'Python é muito filé!'

print('')  # char por char

for letra in texto:
    print(letra, end=' ')
print('')

for n in {1, 2, 3, 4, 4, 4}:  # remove repetido
    print(n, end=' ')

produto = {
    'nome': 'Caneta azul',
    'preço': 8.80,
    'desconto': 0.5
}

for atrib in produto:
    print(atrib, '==>', produto[atrib], end=' ')  # percorre chaves

print('')

for atrib, valor in produto.items():
    print(atrib, '==>', valor, end=' ')
print('')

for valor in produto.values():
    print(valor, end=' ')
print('')

for atrib in produto.keys():
    print(atrib, end=' ')
