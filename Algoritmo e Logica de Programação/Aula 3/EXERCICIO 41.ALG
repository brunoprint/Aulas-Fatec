Algoritmo "semnome"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 01/04/2026
Var
altura:real
peso:real
imc:real


Inicio
      escreva("Digite sua altura:")
      leia(altura)
      escreva("Digite seu peso:")
      leia(peso)
      
      imc <- peso / (altura ^ 2)

      se (imc < 18.5)entao
      escreva("Abaixo do Peso")
      senao
           se(imc >= 18.5) E (imc < 25) entao
           escreva("Peso Normal")
           senao
                se(imc >= 25) E (imc < 30) entao
                escreva("Sobrepeso")
                senao
                     se(imc >= 30) entao
                     escreva("Obesidade")
                     fimse
                fimse
           fimse
      fimse

Fimalgoritmo