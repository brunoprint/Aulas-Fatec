letras = ['A','B','C','D','E']
print(letras)
troca = str(input("Escolha uma das letras acima para ser trocada por 'X' :").upper())

if troca in letras:
    indice = letras.index(troca)
    letras[indice] = 'X'
    print (letras)
else:
    print("Essa letra não está na lista")