programa {
  funcao inicio() {
    inteiro x
    inteiro y
    real resto
    escreva("Digite um número INTEIRO: ")
    leia(x)
    escreva("Digite o denominador(INTEIRO E DIFERENTE DE 0: ")
    leia(y)

    se (y != 0) {
      resto = x % y

      escreva(resto)
    }
    senao {
      escreva("Digite um número diferente de Zero.") 
      }
   

  }
}
