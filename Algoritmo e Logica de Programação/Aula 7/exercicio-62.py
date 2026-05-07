numeros = []
i = 1

while i <= 6:
    num = int(input("Entre com um número: "))
    if num != 0: 
        numeros.append(num)
        for num in numeros:
            print(num)
    i +=1

maior = max(numeros)
posição = numeros.index(maior)
posição +=1
print("O maior número é: ",maior)
print("Sua posição é: ",posição)