cont = 1
soma = 0
while cont <= 10:
    num = int(input("Digite a {} º nota: ".format(cont)))
    soma += num
    cont += 1

media = soma / 10

print("A media é ", media)