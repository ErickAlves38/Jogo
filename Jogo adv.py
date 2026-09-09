import random

print("jogo de adivinhação");
print("tente adivinhar o numero que estou pensando entre 1 a 100");
print("voce tem 7 tetativas para acertar o numero secreto");

numero_secreto = random .randint(1, 100)
contador = 7
acertou = False

while contador > 0:
 tentativa = int(input("adivinhe o numero (1 a 100)"));

print("voce tem", contador, "tentativas");
contador -= 1




if tentativa == numero_secreto:
      print("parabens voce acertou");
      acertou = True
elif tentativa < numero_secreto:
    print("voce errou, o numero secreto é maior que", tentativa);
else:
      print("voce errou, o numero secreto é menor que", tentativa);

print("o numero secreto era", numero_secreto)
