Algoritmo "semnome"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 01/04/2026
Var
   salario:real
   ajuste:real


Inicio
      escreva("digite o salario: ")
      leia(salario)
      
      se (salario < 500) entao
         ajuste <- salario+((salario/100)*15)
         senao
              se (salario >= 500) E (salario <= 1000)entao
              ajuste <- salario+((salario/100)*10)
              senao
              ajuste <- salario+((salario/100)*5)
              fimse
      fimse
      
      escreva("O reajuste salarial foi de: ", salario ," para :", ajuste')


Fimalgoritmo