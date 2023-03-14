import requests
import MarcasIterator
import ModelosIterator
import ModeloAnoIterator
import ModeloEspecificoIterator

# Simula que a requisição está sendo chamada através do navegador, esse tratamento evita o erro 406
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
    codigo = 0
    marcas = MarcasIterator.MarcasIterator(opcao)
    for marca in marcas:
        print("Código: ", marca['codigo'], " Nome: ", marca['nome'])

    codigo = int(input("\nInforme o código a marca: "))
    consultar_marca(opcao, codigo)


def consultar_marca(opcao, marca):
    codigo = 0
    modelos = ModelosIterator.ModelosIterator(opcao, marca)
    for modelo in modelos:
        print("Código: ", modelo['codigo'], " Nome: ", modelo['nome'])

    codigo = int(input("\nInforme o codigo do modelo: "))
    consultar_modelo_ano(opcao, marca, codigo)


def consultar_modelo_ano(opcao, marca, modelo):
    year = ''
    anos = ModeloAnoIterator.ModeloAnoIterator(opcao, marca, modelo)
    for ano in anos:
        print(" Ano: ", ano['nome'], " Código: ", ano['codigo'])

    year = input("\nInforme o código do ano do modelo: ")
    listar_modelo(opcao, marca, modelo, year)


def listar_modelo(opcao, marca, modelo, ano):
    modeloEspecifico = ModeloEspecificoIterator.ModeloEspecificoIterator(
        opcao, marca, modelo, ano)
    print("======================")
    print("Marca: ", modeloEspecifico.modelo['Marca'])
    print("Modelo: ", modeloEspecifico.modelo['Modelo'])
    print("Valor: ", modeloEspecifico.modelo['Valor'])
    print("Ano Modelo: ", modeloEspecifico.modelo['AnoModelo'])
    print("Combustível: ", modeloEspecifico.modelo['Combustivel'])
    print("Codigo Fipe: ", modeloEspecifico.modelo['CodigoFipe'])
    print("Mês de referência: ", modeloEspecifico.modelo['MesReferencia'])
    print("======================\n")


menu_Fipe()
