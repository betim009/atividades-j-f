tempo = int(input("Informe o tempo de conclusão (minutos): "))
idade = int(input("Informe a idade do participante: "))
genero = input("Informe o gênero (M/F): ")
tipo_corrida = input("Informe o tipo de corrida (Trilha/Asfalto/Híbrida): ")
recorde_quebrado = input("Quebrou recorde oficial? (S/N): ")
infracao = input("Cometeu infração? (Corte de caminho/Recebeu ajuda/Nenhuma): ")

# Pontuação base pelo tempo
if tempo < 30:
    pontos = 100
elif 30 <= tempo <= 60:
    pontos = 100 - (tempo - 30) * (30 / 30)  # Decresce de 100 a 70
elif 60 < tempo <= 90:
    pontos = 70 - (tempo - 60) * (30 / 30)  # Decresce de 70 a 40
else:
    pontos = 40

# Pontuação por idade
if idade < 18:
    pontos += 20
elif 18 <= idade <= 30:
    pontos += 10
elif 31 <= idade <= 45:
    pontos += 15
elif 46 <= idade <= 60:
    pontos += 20
else:
    pontos += 25

# Pontuação por gênero
if genero.upper() == "F":
    pontos += 5

# Bonificação por tipo de corrida
if tipo_corrida.lower() == "trilha":
    pontos *= 1.1
elif tipo_corrida.lower() == "híbrida":
    km_trilha = int(input("Quantos km foram percorridos em trilha? "))
    pontos *= 1 + (0.05 * km_trilha)

# Bonificação por quebra de recorde
if recorde_quebrado.upper() == "S":
    pontos += 50

# Penalizações por infração
if infracao.lower() == "corte de caminho":
    pontos -= 10
elif infracao.lower() == "recebeu ajuda":
    pontos = 0  # Desqualificação

print(f"Pontuação final: {pontos}")
