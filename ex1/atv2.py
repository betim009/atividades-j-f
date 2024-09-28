# Pede ao usuário para informar a velocidade máxima permitida na estrada
velocidade_maxima = int(input("Informe a velocidade máxima permitida (km/h): "))

# Pede ao usuário para informar a velocidade atual do veículo
velocidade_veiculo = int(input("Informe a velocidade do veículo (km/h): "))

# Verifica se a velocidade do veículo está dentro do limite permitido
if velocidade_veiculo <= velocidade_maxima:
    # Se a velocidade do veículo for menor ou igual à velocidade máxima, está tudo certo
    print("Velocidade dentro do limite.")
else:
    # Se a velocidade for maior que a máxima permitida, calcula o excesso
    excesso = (
        velocidade_veiculo - velocidade_maxima
    )  # Calcula quantos km/h o veículo está acima do limite

    # Calcula o percentual de excesso com relação à velocidade máxima
    percentual_excesso = (excesso / velocidade_maxima) * 100

    # Verifica em qual faixa de excesso o veículo se encontra e aplica a multa correspondente
    if percentual_excesso <= 20:
        # Se o excesso for até 20%, a multa é de R$ 130,00
        print("Multa de R$ 130,00.")
    elif 20 < percentual_excesso <= 50:
        # Se o excesso for entre 20% e 50%, a multa é de R$ 200,00
        print("Multa de R$ 200,00.")
    else:
        # Se o excesso for maior que 50%, a multa é de R$ 500,00 e a habilitação é suspensa
        print("Multa de R$ 500,00. Habilitação suspensa.")
