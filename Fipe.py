import requests

#Simula que a requisição está sendo chamada através do navegador, esse tratamento evia o erro 406
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def menu_Fipe():
    while True:
        print('------- MENU CONSULTA FIPE -------')
        print('1. Carros')
        print('2. Motos')
        print('3. Caminhoes')
        print('0. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            consultar('carros')
        elif opcao == '2':
            consultar('motos')
        elif opcao == '3':
            consultar('caminhoes')
        elif opcao == '0':
            break
        else:
            print('Opção inválida. Tente novamente.')


def consultar(opcao):
    url = f'https://parallelum.com.br/fipe/api/v1/{opcao}/marcas'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for marca in data:
            print("Código: ", marca['codigo'], " Nome: ", marca['nome'])
        codigo = int(input("\nInforme o código a marca: "))
        consultar_marca(opcao, codigo)
    else:
        print("Erro ao consultar tipo: ", response.status_code)


def consultar_marca(opcao, marca):
    url_marca = f"https://parallelum.com.br/fipe/api/v1/{opcao}/marcas/{marca}/modelos"
    response = requests.get(url_marca, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for modelo in data['modelos']:
            print("ID: ", modelo['codigo'], " Modelo :", modelo['nome'])

        modelo = int(input("\nInforme o codigo do modelo: "))

        for ano in data['anos']:
            print(" Ano: ", ano['nome'], " Código: ", ano['codigo'])

        ano = input("\nInforme o código do ano do modelo: ")

        consultar_modelo(opcao, marca, modelo, ano)
    else:
        print("Erro ao consultar marca: ", response.status_code)


def consultar_modelo(opcao, marca, modelo, ano):
    url_modelo = f"https://parallelum.com.br/fipe/api/v1/{opcao}/marcas/{marca}/modelos/{modelo}/anos/{ano}"
    response = requests.get(url_modelo, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print("======================")
        print("Marca: ", data['Marca'])
        print("Modelo: ", data['Modelo'])
        print("Valor: ", data['Valor'])
        print("Ano Modelo: ", data['AnoModelo'])
        print("Combustível: ", data['Combustivel'])
        print("Codigo Fipe: ", data['CodigoFipe'])
        print("Mês de referência: ", data['MesReferencia'])
        print("======================\n")
    else:
        print("\n================================================")
        print("Modelo não encontrado no ano específico: ", response.status_code)
        print("==================================================\n")


menu_Fipe()
