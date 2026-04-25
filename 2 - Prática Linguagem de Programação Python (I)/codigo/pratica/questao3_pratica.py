# calculadora, metrica / aprendizado padrao para qualquer linguagem, implementada em python

def calc_media(n1, n2):
    return (n1+n2) / 2


def verificar_situacao(media, frequencia):
    # caso a freq. seja menor que entre 60 e 75, o aluno deve tirar 8 pra cima
    if media >= 8 and 60 <= frequencia < 75:
        return "aprovado por nota"
    elif media >= 6 and frequencia >= 75:
        return "aprovado"
    elif media >= 5 and frequencia >= 75:
        return "recuperacao"
    else:
        return "reprovado"


nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
frequencia = float(input("digite a frequencia em porcentagem (ex:75% = 75): "))

media = calc_media(nota1, nota2)
situacao = verificar_situacao(media, frequencia)

# exibe a média formatada com 2 casas decimais
print(f"a media do aluno é: {media:.2f}")
print(f"situacao do aluno: {situacao}")
