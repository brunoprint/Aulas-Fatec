import random

print("-------------")
print("  BetJunior  ")
print("-------------")

segredo = random.randrange(1,11)

acertou = False
tentativas = 3
i = 1

while i<= 3 :
    i +=1
    print("Você possui", tentativas ," tentativas restantes")
    numero = int(input("Digite um número entre 1 e 10: "))

    if numero > 10 or numero < 0:
        print("Digite um número entre 1 e 10")
        i -= 1
        tentativas += 1
    if numero == segredo:
        acertou = True
    if acertou:
        print("-------------------")
        print("    Você acertou   ")
        print("-------------------")
        break
    else:
        print("Você errou")
        tentativas -= 1