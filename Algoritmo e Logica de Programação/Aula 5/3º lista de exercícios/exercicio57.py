maior = None
i=1
while i <=7 :
    num = float(input("Digite um número: "))
    if maior is None:
        maior = num
    else:
        if num > maior:
            maior = num
    i += 1
print("O maior número é: ",maior)
