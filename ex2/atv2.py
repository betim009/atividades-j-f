import random

# Define o nível de dificuldade
nivel = input("Escolha o nível de dificuldade (fácil, médio, difícil): ").lower()

# Determina o intervalo de números com base no nível
if nivel == "fácil":
    numero_aleatorio = random.randint(1, 10)
elif nivel == "médio":
    numero_aleatorio = random.randint(1, 50)
elif nivel == "difícil":
    numero_aleatorio = random.randint(1, 100)
else:
    print("Nível inválido! Por favor, escolha entre fácil, médio ou difícil.")
    exit()

tentativas = 0
while True:
    chute = int(input("Digite seu chute: "))
    tentativas += 1

    if chute == numero_aleatorio:
        print(
            f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativas."
        )
        break
    elif chute < numero_aleatorio:
        print("Seu chute foi menor que o número.")
    else:
        print("Seu chute foi maior que o número.")
