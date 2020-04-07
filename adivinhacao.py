from math import *
import random

number = random.randrange(1, 101)
print(number)
# Seleciona nível
tentativas = 1
valida_nivel = True
while valida_nivel:
    nivel = int(input("Selecione a dificuldade: Fácil(1); Médio(2); Difícil(3)"))

    if nivel == 1:
        tentativas = 10
        print('Você está no nível fácil e possui 10 chanches')
        break
    if nivel == 2:
        tentativas = 5
        print('Você está no nível médio e possui 5 chanches')
        break
    if nivel == 3:
        tentativas = 3
        print('Você está no nível difícil e possui 3 chanches')
        break
    if nivel != 1 and nivel != 2 and nivel != 3:
        print("SELECIONE UM NÍVEL!!")


pontos = 1000

# Testa chute
for tentativas in range(1, tentativas + 1):
    chute = int(input("Digite seu chute: "))
    if chute == number:
        print("Você acertou!!!!")
        break
    else:
        if number > chute:
            print("Chute um número maior!!")
        elif number < chute:
            print("Chute um número menor!!")
    pontos_perdidos = abs(chute - number)
    pontos -= pontos_perdidos

print("Sua pontuação foi: {}".format(pontos))
print("FIM DE JOGO!!!")
