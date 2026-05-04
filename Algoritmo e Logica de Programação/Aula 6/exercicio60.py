numeros = [0]
i = 1

while i > 0:
    num = int(input("Entre com um número: "))
    if num != 0: 
        print("Lista Atualizada...")
        numeros.append(num)
        numeros.sort()
        for num in numeros:
            print(num)
    else:
        print("Programa Encerrado")
        break