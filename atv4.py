def calcular_preco(idade):
    if idade <= 17:
        return 15
    elif 18 <= idade <= 59:
        return 30
    else:
        return 20


idade1 = int(input("Informe a idade da primeira pessoa: "))
idade2 = int(input("Informe a idade da segunda pessoa: "))

preco1 = calcular_preco(idade1)
preco2 = calcular_preco(idade2)

total = preco1 + preco2

print(f"O total a ser pago pelos ingressos é R$ {total:.2f}")
