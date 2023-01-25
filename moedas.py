from requests import get
import json

cotacoes = get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
moedas = cotacoes.json()
dolar = moedas['USDBRL']
euro = moedas['EURBRL']
bitcoin = moedas['BTCBRL']


def conv_dolar(valor):
    print('-' * 25)
    print('      $ Dolar $       ')
    print(f'Cotação Atual: R$ {float(dolar["high"]):.2f}')
    print(f'R$ {valor:.2f} => $ {valor / float(dolar["high"]):.2f}')
    print(f'{dolar["create_date"]}')
    print('-' * 25)


def conv_euro(valor):
    print('-' * 25)
    print('      € Euro €       ')
    print(f'Cotação Atual: R$ {float(euro["high"]):.2f}')
    print(f'R$ {valor:.2f} => € {valor / float(euro["high"]):.2f}')
    print(f'{euro["create_date"]}')
    print('-' * 25)


def libraES(valor):
    libraES = 6.53
    print('-' * 25)
    print(' £ Libra Esterlina £ ')
    print(f'Cotação atual: R$ {libraES}')
    print(f'R$ {valor:.2f} => £ {valor / libraES:.2f}')
    print('-' * 25)


def conv_bitcoin(valor):
    print('-' * 25)
    print(' ₿ Bitcoin ₿ ')
    print(f'Cotação atual: R$ {float(bitcoin["high"]):.2f}')
    print(f'R$ {valor:.2f} => ₿ {valor / float(bitcoin["high"]):.2f}')
    print(f'{bitcoin["create_date"]}')
    print('-' * 25)
