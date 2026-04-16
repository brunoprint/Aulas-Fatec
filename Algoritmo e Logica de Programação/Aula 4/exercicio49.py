prod1 = int(input("Digite o preço do produto 1: "))
prod2 = int(input("Digite o preço do produto 2: "))

desc1 = prod1-((prod1/100)*8)
desc2 = prod2-((prod2/100)*11)
total = desc1 + desc2

print("")
print("O valor do produto 1 com desconto é de: ", desc1)
print("O valor do produto 2 com desconto é de: ", desc2)
print("O preço total sera de: ", total)
print("")