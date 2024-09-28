while True:
    numero = int(input("Digite um número inteiro positivo: "))

    if numero < 0:
        print("Número negativo digitado. Programa encerrado.")
        break

    contagem_impares = 0
    soma_impares = 0

    for i in range(1, numero + 1):
        if i % 2 != 0:
            contagem_impares += 1
            soma_impares += i

    print(f"Total de números ímpares: {contagem_impares}")
    print(f"Soma dos números ímpares: {soma_impares}")
