from random import randint

nome = str(input('qual seu nome? '))
escolhas = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''suas opções:
(0) pedra
(1) papel
(2) tesoura''')
jogador = int(input(f'{nome} qual é a sua jogada? '))
print('-' * 30)
print(f'computador jogou {escolhas[computador]}')
print(f'{nome} jogou {escolhas[jogador]}')
print('-' * 30)

if computador == jogador:
    print('empate!')

elif computador == 0 and jogador == 1:
    print(f'{nome} venceu!!!')
elif computador == 0 and jogador == 2:
    print('computador venceu!')
elif computador == 1 and jogador == 0:
    print('computador venceu!')
elif computador == 1 and jogador == 2:
    print(f'{nome} venceu!!!')
elif computador == 2 and jogador == 1:
    print('computador venceu!')
elif computador == 2 and jogador == 0:
    print(f'{nome} venceu!!!')


