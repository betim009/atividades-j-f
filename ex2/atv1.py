# Solicita o salário inicial e o ano de contratação do funcionário
salario_inicial = float(input("Digite o salário inicial (R$): "))
ano_contratacao = int(input("Digite o ano de contratação: "))

# Verifica se o salário inicial é maior ou igual a R$ 1000,00
if salario_inicial < 1000:
    print("O salário inicial deve ser maior ou igual a R$ 1000,00.")
else:
    # Verifica se o ano de contratação está entre 1995 e o ano atual (2024)
    if 1995 <= ano_contratacao <= 2024:
        # Define as variáveis iniciais
        ano_atual = 2024
        anos_trabalhados = ano_atual - ano_contratacao
        salario_atual = salario_inicial
        percentual_aumento = 1.5  # Percentual de aumento inicial

        # Calcula o aumento para cada ano trabalhado
        for ano in range(anos_trabalhados):
            salario_atual += salario_atual * (percentual_aumento / 100)
            percentual_aumento += percentual_aumento * 0.1  # Aumento progressivo

        # Calcula o aumento percentual total
        aumento_percentual = ((salario_atual - salario_inicial) / salario_inicial) * 100

        # Exibe o salário atual e o aumento percentual
        print(f"Salário atual: R${salario_atual:.2f}")
        print(f"Aumento percentual: {aumento_percentual:.2f}%")
    else:
        print("O ano de contratação deve estar entre 1995 e 2024.")
