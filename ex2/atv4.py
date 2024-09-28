while True:
    numero = int(input("Digite um número inteiro positivo (ou negativo para sair): "))
    
    if numero < 0:
        print("Programa encerrado.")
        break

    # Verificar se o número é par ou ímpar
    if numero % 2 == 0:
        print("O número é Par.")
    else:
        print("O número é Ímpar.")

    # Verificar se o número é primo
    if numero < 2:
        print("O número não é Primo.")
    else:
        primo = True
        for i in range(2, numero):
            if numero % i == 0:
                primo = False
                break
        if primo:
            print("O número é Primo.")
        else:
            print("O número não é Primo.")

    # Verificar se o número é de Armstrong
    temp = numero
    soma = 0
    while temp > 0:
        digito = temp % 10
        soma += digito ** 3
        temp //= 10

    if soma == numero:
        print("O número é de Armstrong.")
    else:
        print("O número não é de Armstrong.")

    # Verificar se é um quadrado perfeito
    raiz = int(numero ** 0.5)
    if raiz * raiz == numero:
        print("O número é um Quadrado Perfeito.")
    else:
        print("O número não é um Quadrado Perfeito.")

    # Verificar se é um palíndromo
    numero_str = str(numero)
    if numero_str == numero_str[::-1]:
        print("O número é um Palíndromo.")
    else:
        print("O número não é um Palíndromo.")

    # Verificar se o número está na sequência de Fibonacci
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b

    if b == numero or numero == 0:
        print("O número está na sequência de Fibonacci.")
    else:
        print("O número não está na sequência de Fibonacci.")

    print("--------------------------------------------------")
