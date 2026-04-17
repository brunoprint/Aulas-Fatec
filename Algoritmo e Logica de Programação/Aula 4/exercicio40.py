nota1 = int(input("Digite a 1º nota: "))
nota2 = int(input("Digite a 2º nota: "))
nota3 = int(input("Digite a 3º nota: "))

media = (nota1 + nota2 + nota3) / 3

if media > 7:
    print("Parabéns, você passou!")
else:
    print("Você reprovou")