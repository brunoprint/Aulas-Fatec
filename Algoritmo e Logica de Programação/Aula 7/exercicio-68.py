n = float(input("Digite o primeiro termo: "))
r = float(input("Digite a razão: "))

i=1
while i <=5:
    print(n)
    if r > 0:
        n = n * r
    elif 0 < r < 1:
        n = n / r
    elif r < 0:
        n = n * r
    elif r is 1:
        n = n
    i+=1
    