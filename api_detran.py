import requests

# url da api - site: infosimples.com
url = 'https://api.infosimples.com/api/v2/consultas/detran/pi/licenciamento'
args = {
    "placa": "QRU9J95",
    "renavam": "01269680827",
    "exercicio": "",
    "token": "FrFyf0Xv62Wq_OBQCMlMEn9_Gex88CerY9gPq-Np",
    "timeout": 300
}

# convertendo para json
response = requests.post(url, args)
response_json = response.json()
header = response_json['header']  # cabeçlho contendo parametros, cliente etc.
data = response_json['data'][0]  # dados do veículo (licenciamento e multas)
response.close()

# condição caso dê certo - cod 200.
if response_json['code'] == 200:
    print('-' * 42)
    print(header['service'])
    print(f'Cliente: {header["client_name"]}')
    for chave, valor in header['parameters'].items():
        print(f'{chave}: {valor}')
    print('-' * 42)

    # -----------------------------------------------------------

    print(f'*- Taxas: {len(data["licenciamento"])} encontrada(s) -*')
    for chave in data['licenciamento']:
        for c, v in chave.items():
            print(f'{c}: {v}')
    print('-' * 42)

    # -----------------------------------------------------------

    print(f'*- Multas: {len(data["multas"])} encontrada(s) -*')
    for chave in data['multas']:
        for c, v in chave.items():
            print(f'{c}: {v}')
        print('-' * 42)

    # -----------------------------------------------------------

# condição caso não dê certo - cod 600 à 799.
elif response_json['code'] in range(600, 799):
    mensagem = "Resultado sem sucesso. Leia para saber mais: \n"
    mensagem += f"Código: {response_json['code']} ({response_json['code_message']})\n"
    mensagem += "; ".join(response_json['errors'])
    print(mensagem)
