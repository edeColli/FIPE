import requests

# Simula que a requisição está sendo chamada através do navegador, esse tratamento evita o erro 406
headers = {'User-Agent': 'MyAppFipe/1.0'}


class ModeloEspecificoIterator:
    def __init__(self, option: str, marca: str, modelo: str, ano: str):

        url_marcas = f"https://parallelum.com.br/fipe/api/v1/{option}/marcas/{marca}/modelos/{modelo}/anos/{ano}"
        response = requests.get(url_marcas, headers=headers)
        if response.status_code == 200:
            self.modelo = response.json()
            self.current = 0
            self.end = len(self.modelo)
        else:
            raise Exception(
                f"Modelo não encontrado no ano específico: ", response.status_code)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = list(self.modelo)[self.current]
        self.current += 1
        return result
