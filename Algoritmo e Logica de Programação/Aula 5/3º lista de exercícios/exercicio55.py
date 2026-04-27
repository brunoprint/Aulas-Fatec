quant = int(input("Digite quantas notas irão ser: "))
i = 1
nota = 0 
x = 0
while i <= quant:
    nota = float(input("Digite a {}º nota: ".format(i)))
    x += nota
    i += 1

media = x / quant

print("A média é ",media)