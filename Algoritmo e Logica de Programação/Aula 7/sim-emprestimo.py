import os
def limpart_tela():
    os.system('cls' if os.name == 'nt' else 'clear') 

rep = "s"
while rep == "s":
    if rep == "s":
        limpart_tela()


        print("---------------------------------")
        print("   Seja Bem-Vindo(a) ao MyBank   ")
        print("---------------------------------")

        cliente = str(input("Você já é nosso cliente? s/n: ").lower())
        if cliente == "n":
            score = int(input("Digite seu Serasa Score: "))
        valor = float(input("Valor desejado para o empréstimo: "))
        quantparc = int(input("Quantidade de Parcelas: "))
        seg = str(input("Deseja incluir um seguro desemprego no seu empréstimo? s/n: ").lower())

        #calculo com IOF
        iof = valor * 0.0038

        if seg == "s":
            valor += 50

        #juros por score
        if cliente == "n":
            valor += 35
            if 0 <= score <= 299:
                taxa = 0.2
            elif 300 <= score <= 499:
                taxa = 0.15
            elif 500 <= score <= 699:
                taxa = 0.1
            elif 700 <= score <= 1000:
                taxa = 0.05
        else:
            taxa = 0.05
    
        #cet
        valor = valor + iof
        cet = valor + (valor * taxa)

        valparc = cet / quantparc

        taxa = taxa * 100
        print("----------------------------------")
        print("      RESULTADO DA SIMULAÇÃO      ")
        print("----------------------------------")

        print("Quantidade de parcelas: ",quantparc)
        print("Valor das parcelas: ",f'{valparc:.2f}')  
        print("Taxa de juros: ",taxa,"%")
        print("Custo Efetivo Total: ",cet)


        rep = str(input("Deseja realizar outra simulação? s/n: ").lower())
        if rep == "n":
            print("Programa Encerrado")