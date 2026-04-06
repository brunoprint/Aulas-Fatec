Algoritmo "semnome"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 01/04/2026
Var
mens:real
pag:inteiro
final:real



Inicio
      Escreva("Escreva o valor da mensalidade: ")
      leia(mens)
      
      Escreva("Qual a forma de pagamento? 1-cartão ; 2-pix ; 3-dinheiro :")
      leia(pag)
      
      se(pag = 1)entao
      Escreva("O valor da mensalidade é de: ", mens)
      senao
           se(pag = 2)entao
           final <- mens-((mens/100)*6)
           escreva("O valor da mensalidade é de: ", final)
           senao
           final <- mens-(mens/10)
           escreva("O valor da mensalidade é de: ", final)
           fimse
      fimse


Fimalgoritmo