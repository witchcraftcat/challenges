

def calculo_notas():
    valor_notas = 0
    quant_notas = int(input("Digite a quantidade de notas a serem computadas: "))
    for cont in range(1, quant_notas + 1):
        nota = float(input(f'Digite a {cont} nota: '))
        valor_notas += nota

    media = valor_notas/quant_notas
    print(media)

calculo_notas()





