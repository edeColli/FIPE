# FIPE

* Para listar as marcas use a URL:  https://parallelum.com.br/fipe/api/v1/carros/marcas dessa forma serão listadas todas as marcas que a API possui. 
* Escolha uma para ser usada na próxima etapa, grave o ID dela para ser usado no seu código.
* Nesta etapa use a marca selecionada para poder retornar os veículos que essa marca possui usando a URL: 
** https://parallelum.com.br/fipe/api/v1/carros/marcas/{ID_MARCASELECIONADA}/modelos
* Ao chamar esse endpoint, será retornada uma resposta que possui um nó, no formato JSON, com os modelos dos veículos que ela possui.
* Seu interator deverá inteirar em cada um desses modelos e trazer informações do nome e ID do veículo da marca selecionada.
