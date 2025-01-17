def calc_gorjeta():
    valor_conta = float(input("Qual o valor da conta?"))
    valor_gorjeta = float(input("Qual a porcentagem da gorjeta?"))

    porcentagem = (valor_gorjeta / 100) +1

    valor_total = float(porcentagem * valor_conta)

    print(f'O valor da conta é {valor_conta:.2f} e o valor da gorjeta é {valor_gorjeta:.2g}%. Logo, o valor total é {valor_total:.2f}')

calc_gorjeta()



