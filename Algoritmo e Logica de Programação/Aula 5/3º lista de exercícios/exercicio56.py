bruto = int(input("Digite o valor do seu salário: "))

if bruto <= 2428:
    ir = 0
elif 2428 < bruto <= 2826:
    ir = bruto * 0.075
elif 2826 < bruto <= 3751:
    ir = bruto * 0.15
elif 3751 < bruto <= 4664:
    ir = bruto * 0.225
else:
    ir = bruto * 0.275

if bruto <= 1518:
    inss = bruto * 0.075
elif 1518 < bruto <= 2794:
    inss = bruto * 0.09
elif 2794 < bruto <= 4190:
    inss = bruto * 0.12
else:
    inss = bruto * 0.14

liquido = bruto-(ir + inss)

print("O valor bruto é : ",bruto)
print("O valor do IR é : ", ir)
print("O valor do INSS é :", inss)
print("O valor líquido é :", liquido)