# Função que calcula o preço do ingresso com base na idade da pessoa
def calcular_preco(idade):
    # Se a pessoa tem 17 anos ou menos, o preço é 15 reais
    if idade <= 17:
        return 15
    # Se a pessoa tem entre 18 e 59 anos, o preço é 30 reais
    elif 18 <= idade <= 59:
        return 30
    # Se a pessoa tem 60 anos ou mais, o preço é 20 reais
    else:
        return 20


# Solicita a idade da primeira pessoa e converte para um número inteiro
idade1 = int(input("Informe a idade da primeira pessoa: "))

# Solicita a idade da segunda pessoa e converte para um número inteiro
idade2 = int(input("Informe a idade da segunda pessoa: "))

# Calcula o preço do ingresso para a primeira pessoa usando a função 'calcular_preco'
preco1 = calcular_preco(idade1)

# Calcula o preço do ingresso para a segunda pessoa usando a mesma função
preco2 = calcular_preco(idade2)

# Soma os preços dos ingressos das duas pessoas
total = preco1 + preco2

# Exibe o total a ser pago, formatando o valor com duas casas decimais
print(f"O total a ser pago pelos ingressos é R$ {total:.2f}")
