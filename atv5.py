# Solicita o tempo de conclusão da corrida em minutos
tempo = int(input("Informe o tempo de conclusão (minutos): "))

# Solicita a idade do participante
idade = int(input("Informe a idade do participante: "))

# Solicita o gênero do participante, sendo M para masculino e F para feminino
genero = input("Informe o gênero (M/F): ")

# Solicita o tipo de corrida: Trilha, Asfalto ou Híbrida
tipo_corrida = input("Informe o tipo de corrida (Trilha/Asfalto/Híbrida): ")

# Pergunta se o participante quebrou o recorde oficial
recorde_quebrado = input("Quebrou recorde oficial? (S/N): ")

# Pergunta se o participante cometeu alguma infração durante a corrida
infracao = input("Cometeu infração? (Corte de caminho/Recebeu ajuda/Nenhuma): ")

# Agora começamos a calcular a pontuação com base em várias condições

# Pontuação base pelo tempo de conclusão
if tempo < 30:
    # Se o tempo for menor que 30 minutos, ganha 100 pontos
    pontos = 100
elif 30 <= tempo <= 60:
    # Se o tempo for entre 30 e 60 minutos, os pontos diminuem de 100 até 70
    pontos = 100 - (tempo - 30) * (30 / 30)
elif 60 < tempo <= 90:
    # Se o tempo for entre 60 e 90 minutos, os pontos diminuem de 70 até 40
    pontos = 70 - (tempo - 60) * (30 / 30)
else:
    # Se o tempo for maior que 90 minutos, a pontuação base é 40
    pontos = 40

# Pontuação extra pela idade
if idade < 18:
    # Se for menor de 18 anos, adiciona 20 pontos
    pontos += 20
elif 18 <= idade <= 30:
    # Se a idade for entre 18 e 30, adiciona 10 pontos
    pontos += 10
elif 31 <= idade <= 45:
    # Se a idade for entre 31 e 45, adiciona 15 pontos
    pontos += 15
elif 46 <= idade <= 60:
    # Se a idade for entre 46 e 60, adiciona 20 pontos
    pontos += 20
else:
    # Se a idade for maior que 60, adiciona 25 pontos
    pontos += 25

# Pontuação extra pelo gênero
if genero.upper() == "F":
    # Mulheres ganham 5 pontos extras
    pontos += 5

# Bonificação pelo tipo de corrida
if tipo_corrida.lower() == "trilha":
    # Se a corrida for trilha, os pontos aumentam em 10%
    pontos *= 1.1
elif tipo_corrida.lower() == "híbrida":
    # Se for uma corrida híbrida, pergunta quantos km foram percorridos em trilha
    km_trilha = int(input("Quantos km foram percorridos em trilha? "))
    # A pontuação aumenta 5% para cada km percorrido na trilha
    pontos *= 1 + (0.05 * km_trilha)

# Bonificação por quebra de recorde
if recorde_quebrado.upper() == "S":
    # Se o participante quebrou o recorde, ganha 50 pontos extras
    pontos += 50

# Penalizações por infração
if infracao.lower() == "corte de caminho":
    # Se houve corte de caminho, perde 10 pontos
    pontos -= 10
elif infracao.lower() == "recebeu ajuda":
    # Se recebeu ajuda, o participante é desqualificado (pontuação vai a 0)
    pontos = 0

# Exibe a pontuação final do participante
print(f"Pontuação final: {pontos}")
