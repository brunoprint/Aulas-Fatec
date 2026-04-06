Algoritmo "semnome"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 01/04/2026
Var
   nota1:real
   nota2:real
   nota3:real
   media:real


Inicio
      escreva("Digite a nota 1:")
      leia(nota1)
      escreva("Digite a nota 2:")
      leia(nota2)
      escreva("Digite a nota 3:")
      leia(nota3)
      
      media <- (nota1 + nota2 + nota3) / 3
      
      se (media >= 7) entao
        escreva("Parabens! Você foi aprovado!")
        senao
        escreva("Você foi reprovado!")
      fimse


Fimalgoritmo