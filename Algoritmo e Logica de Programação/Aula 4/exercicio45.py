mens = float(input("Digite o valor da mensalidade: "))
pag = str(input("Qual a forma de pagamento?  1- cartão ; 2-pix ; 3-dinheiro "))

if pag == "1":
    final = mens
elif pag == "2":
    final = mens - (mens * 0.06)
else:
    final = mens - (mens * 0.1)

print("O valor final da mensalidade será de ",final," Reais")