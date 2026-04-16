nome = str(input("Digite um nome: "))
nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))

media = (nota1 + nota2)/2

if media >= 7:
    print("Parabéns ",nome,"Voce foi aprovado!")
else:
    print("Voce ficou com média ", media ," e foi reprovado!")