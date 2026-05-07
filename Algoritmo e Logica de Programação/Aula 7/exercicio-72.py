i = 1
maior = None
menor = None
soma = 0

while i <= 10:
    num = int(input("Digite o {}º número: ".format(i)))

    if maior is None or num > maior:
        maior = num

    if menor is None or num < menor:
        menor = num

    soma = soma + num

    i += 1

media = soma / 10


print("Maior número: ",maior)
print("Menor número: ",menor)
print("Soma dos números: ",soma)
print("Média dos número: ",media)