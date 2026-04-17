altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kilos: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc <= 30:
    print("Sobrepeso")
else:
    print("Obesidade")