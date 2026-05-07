print("Escolha uma das operações abaixo: ")
operacao = str(input("A - Soma / B - Substração / C - Multiplicação / D - Divisão :").upper())

num1 = float(input("Digite um número: "))
num2 = float(input("Digite mais um número: "))

if operacao == 'A':
    final = num1 + num2
    print(num1,"+",num2,"=",final)
elif operacao == 'B':
    final = num1 - num2
    print(num1,"-",num2,"=",final)
elif operacao == 'C':
    final = num1 * num2
    print(num1,"X",num2,"=",final)
elif operacao == 'D':
    final = num1 / num2
    print(num1,"/",num2,"=",final)
