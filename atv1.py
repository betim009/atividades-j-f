valor_saque = int(input("Informe o valor do saque: "))

if valor_saque < 10 or valor_saque > 600:
    print("Valor inválido. O saque deve ser entre 10 e 600 reais.")
else:
    # Notas disponíveis
    nota100 = valor_saque // 100
    valor_saque %= 100

    nota50 = valor_saque // 50
    valor_saque %= 50

    nota10 = valor_saque // 10
    valor_saque %= 10

    nota5 = valor_saque // 5
    valor_saque %= 5

    nota2 = valor_saque // 2
    valor_saque %= 2

    # Exibindo o número de notas
    if nota100 > 0:
        print(f"{nota100} nota(s) de 100 reais")
    if nota50 > 0:
        print(f"{nota50} nota(s) de 50 reais")
    if nota10 > 0:
        print(f"{nota10} nota(s) de 10 reais")
    if nota5 > 0:
        print(f"{nota5} nota(s) de 5 reais")
    if nota2 > 0:
        print(f"{nota2} nota(s) de 2 reais")
