numeros = []

i=1

while i <= 5:
    num = int(input("Digite um número: "))
    numeros.append(num)
    numeros.sort()
    i+=1
print("Números Digitados:")
print(numeros)