import random

while True:
    print("----------------------------------")
    print("            BETJunior             ")
    print("----------------------------------")

    segredo = random.randrange(1, 11)

    tentativas = 3

    for i in range(1, 4):
        print("Você possui", tentativas, "Tentativas de 3\n")

        try:
            numero = int(input("Digite um número entre 1 e 10: "))

            if numero < 1 or numero > 10:
                print("Número inválido! Digite entre 1 e 10.\n")
                tentativas -= 1
                continue

        except ValueError:
            print("Digite apenas números!\n")
            tentativas -= 1
            continue

        if numero == segredo:
            print("----------------------------------")
            print("      VOCE ACERTOU!!! PARABENS    ")
            print("----------------------------------")
            break
        else:
            print("Voce errou! Tente novamente\n")
            tentativas -= 1

    print("Fim de Jogo")

    resposta = input("Deseja jogar novamente? (s/n): ").lower()

    if resposta == "n":
        print("Encerrando o jogo...")
        break