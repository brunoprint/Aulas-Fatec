media = float(input("Digite sua média (0-10): "))
freq = int(input("Digite sua frequência (0-100): "))

if freq < 75:
    print("Você foi reprovado!")
else:   
    if freq > 75 and media < 7:
        print("Você está de recuperação!")
    else:
        print("Você foi aprovado!")