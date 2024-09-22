velocidade_maxima = int(
    input("Informe a velocidade máxima permitida (km/h): "))
velocidade_veiculo = int(
    input("Informe a velocidade do veículo (km/h): "))

if velocidade_veiculo <= velocidade_maxima:
    print("Velocidade dentro do limite.")
else:
    excesso = velocidade_veiculo - velocidade_maxima
    percentual_excesso = (excesso / velocidade_maxima) * 100

    if percentual_excesso <= 20:
        print("Multa de R$ 130,00.")
    elif 20 < percentual_excesso <= 50:
        print("Multa de R$ 200,00.")
    else:
        print("Multa de R$ 500,00. Habilitação suspensa.")
