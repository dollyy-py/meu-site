import random
numero_secreto = random.randint(1, 10)
while True:
    chute = int(input('Digite um número entre 1 e 10:'))
    if chute == numero_secreto:
        print('parabens, você acertou!')
        break
    else:
        print('tente novamente!')