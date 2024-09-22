numeros = []

for i in range(3):
    numero = int(input(f"Informe o {i+1}º número: "))
    numeros.append(numero)

menor = min(numeros)
maior = max(numeros)

numeros_ordenados = sorted(numeros)

print(f"Menor número: {menor}")
print(f"Maior número: {maior}")
print(f"Números em ordem crescente: {numeros_ordenados}")
