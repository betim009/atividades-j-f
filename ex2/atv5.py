# Solicita o valor da dívida e o valor que o cliente pode pagar mensalmente
valor_divida = float(input("Digite o valor total da dívida (R$): "))
valor_mensal = float(input("Digite o valor que o cliente pode pagar por mês (R$): "))

mes = 0
while valor_divida > 0:
    mes += 1
    print(f"Mês {mes}: Dívida antes do pagamento: R${valor_divida:.2f}")
    
    if valor_mensal > valor_divida:
        valor_mensal = valor_divida

    valor_divida -= valor_mensal
    print(f"Mês {mes}: Dívida após o pagamento: R${valor_divida:.2f}\n")

print("Dívida quitada com sucesso!")
