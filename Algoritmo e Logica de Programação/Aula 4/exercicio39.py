salario = int(input("Digite o valor do salário para reajuste: "))

if salario < 500:
    reajuste = salario + (salario * 0.15)

elif 500 <= salario <= 1000:
    reajuste = salario * 1.1

else:
    reajuste = salario + (salario / 20)

print("Seu salario com rejuste será de ", reajuste)