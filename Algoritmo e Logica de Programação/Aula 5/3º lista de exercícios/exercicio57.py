maior = None

for i in range(7):
    num = float(input("Digite um número: "))

    if maior is None or num > maior:
        maior = num

print("O maior númeor é: ", maior)