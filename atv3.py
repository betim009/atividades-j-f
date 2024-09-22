# Cria uma lista vazia chamada 'numeros' para guardar os números que o usuário vai digitar
numeros = []

# Usa um loop para pedir três números ao usuário
for i in range(3):
    # Pede ao usuário para informar um número, um de cada vez
    numero = int(input(f"Informe o {i+1}º número: "))
    # Adiciona o número que o usuário digitou na lista 'numeros'
    numeros.append(numero)

# A seguir, encontramos o menor e o maior número da lista

# 'min' encontra o menor número da lista
menor = min(numeros)

# 'max' encontra o maior número da lista
maior = max(numeros)

# 'sorted' organiza os números em ordem crescente e os salva na variável 'numeros_ordenados'
numeros_ordenados = sorted(numeros)

# Exibe o menor número da lista
print(f"Menor número: {menor}")

# Exibe o maior número da lista
print(f"Maior número: {maior}")

# Exibe todos os números em ordem crescente
print(f"Números em ordem crescente: {numeros_ordenados}")
