nome = str(input("Digite seu nome: "))
nota1 = int(input("Digite a 1º nota: "))
nota2 = int(input("Digite a 2º nota: "))
nota3 = int(input("Digite a 3º nota: "))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print("Parabéns ", nome , "!Você foi aprovado!")

elif 5>=media<7:
    print("Você ficou com média ", media ," e está de recuperação.")

else:
    print( nome ,".Você está reprovado.")