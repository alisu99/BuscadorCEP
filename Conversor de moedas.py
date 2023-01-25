# conversor de moedas 3.0
from moedas import *
from time import sleep


valor = float(input('Saldo R$: '))
opcao = 0
print(
f'''----- Saldo R$ {valor:.2f} -----
[1] Dolar
[2] Euro
[3] Bitcoin
[4] Alterar Saldo''')


while opcao != 5:
    opcao = int(input('Opção desejada ([5] para sair): '))
    if opcao == 1:
        conv_dolar(valor)
        sleep(1)

    elif opcao == 2:
        conv_euro(valor)
        sleep(1)

    elif opcao == 3:
        conv_bitcoin(valor)
        sleep(1)

    elif opcao == 4:
        print('-' * 25)
        valor = float(input('Saldo: '))
        print(
f'''----- Saldo R$ {valor:.2f} -----
[1] Dolar
[2] Euro
[3] Libra esterlina
[4] Alterar Saldo
____________________________________''')
        sleep(1)

    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('\033[0:31mOpção inválida, tente novamente!\033[0:0m')

