# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.

nmr1 = int(input("Digite o primeiro número: "))
nmr2 = int(input("Digite o segundo número: "))
operacao = str(input("""(Digite qual operação você quer)
  soma
  subtração
  multiplicação
  divisão
  [Digite]:   """))


if operacao == "soma":
    print("Seu resultado é: ", nmr1 + nmr2)
elif operacao == "subtração":
    print("Seu resultado é ", nmr1 - nmr2)
elif operacao == "multiplicação":
    print("Seu resultado é: ", nmr1 * nmr2)
elif operacao == "divisão":
    print("Seu resultado é: ", nmr1/nmr2)    
