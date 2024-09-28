# Solicita ao usuário que informe o valor que deseja sacar
valor_saque = int(input("Informe o valor do saque: "))

# Verifica se o valor do saque está entre 10 e 600 reais
# Se o valor for menor que 10 ou maior que 600, exibe uma mensagem de erro
if valor_saque < 10 or valor_saque > 600:
    print("Valor inválido. O saque deve ser entre 10 e 600 reais.")
else:
    # As próximas linhas vão calcular quantas notas de cada valor serão necessárias

    # Calcula quantas notas de 100 reais são necessárias
    nota100 = (
        valor_saque // 100
    )  # Divide o valor do saque por 100 e pega apenas a parte inteira (quantidade de notas)
    valor_saque %= (
        100  # Atualiza o valor do saque com o que sobrou após retirar as notas de 100
    )

    # Calcula quantas notas de 50 reais são necessárias
    nota50 = (
        valor_saque // 50
    )  # Divide o valor restante por 50 e pega a quantidade de notas
    valor_saque %= (
        50  # Atualiza o valor do saque com o que sobrou após retirar as notas de 50
    )

    # Calcula quantas notas de 10 reais são necessárias
    nota10 = valor_saque // 10  # Mesma lógica, agora para as notas de 10 reais
    valor_saque %= 10  # Atualiza o valor do saque

    # Calcula quantas notas de 5 reais são necessárias
    nota5 = valor_saque // 5  # Mesma lógica para as notas de 5 reais
    valor_saque %= 5  # Atualiza o valor do saque

    # Calcula quantas notas de 2 reais são necessárias
    nota2 = valor_saque // 2  # E agora para as notas de 2 reais
    valor_saque %= 2  # Atualiza o valor do saque

    # A seguir, vamos exibir quantas notas de cada valor foram usadas

    # Se houver pelo menos 1 nota de 100, mostra essa informação
    if nota100 > 0:
        print(f"{nota100} nota(s) de 100 reais")

    # Se houver pelo menos 1 nota de 50, mostra essa informação
    if nota50 > 0:
        print(f"{nota50} nota(s) de 50 reais")

    # Se houver pelo menos 1 nota de 10, mostra essa informação
    if nota10 > 0:
        print(f"{nota10} nota(s) de 10 reais")

    # Se houver pelo menos 1 nota de 5, mostra essa informação
    if nota5 > 0:
        print(f"{nota5} nota(s) de 5 reais")

    # Se houver pelo menos 1 nota de 2, mostra essa informação
    if nota2 > 0:
        print(f"{nota2} nota(s) de 2 reais")
