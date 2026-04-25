a = 3
b = 4.4
print(a + b)  # 7.4

texto = 'Sua idade é...: '
idade = 23  # padrao

# print(texto + str(idade))
print(f'{texto} {idade}')

saudacao = 'bom dia'
print(3 * saudacao)  # repete string 3 vezes bom diabom diabom dia

PI = 3.14
raio = float(input('Informe o raio da circ? '))
area = PI * pow(raio, 2)  # pow = potencia

print(type(raio))  # float
print(f'A area da circunferencia é: {area} m2.')
