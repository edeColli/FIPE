import requests

# Simula que a requisição está sendo chamada através do navegador, esse tratamento evita o erro 406
headers = {'User-Agent': 'MyAppFipe/1.0'}


class MarcasIterator:
    def __init__(self, option: str):

        url_marcas = f"https://parallelum.com.br/fipe/api/v1/{option}/marcas"
        response = requests.get(url_marcas, headers=headers)
        if response.status_code == 200:
            self.marcas = response.json()
            self.current = 0
            self.end = len(self.marcas)
        else:
            raise Exception(f"Erro ao carregar marcas: {response.status_code}")

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = list(self.marcas)[self.current]
        self.current += 1
        return result
