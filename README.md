# Scrapper Pokemon
### Programa feito para a matéria de Ciência de Dados do 6° Semestre de Ciência da Computação

### Por Caroline Viana e Richard Santino

---

## Descrição
O projeto é a construção de um Scrapper que navega por duas pokedex, extraindo os dados de cada um dos pokemons, para salvá-los num arquivo final CSV.

Foi utilizada a biblioteca Scrapy para a extração desses dados, e a biblioteca Pandas para o tratamento deles.

## Conteúdo e execução

O repositório já possui o CSV com as informações já extraidas, podendo ser vistas no `pokemonData.csv`.

Mas caso deseje executar o programa desde o começo, e gerar todos os arquivos do zero, siga as etapas:

O projeto possui cinco arquivos necessários para sua execução:
- `main.py`: arquivo principal de tratamento;
- `bulbapediaScrapper.py`: Scrapper para a pokedex [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number);
- `serebiScrapper.py`: Scrapper para a pokedex [Serebii](https://www.serebii.net/pokemon/nationalpokedex.shtml);
- `pandasBulbapedia.py`: Tratamento dos dados extraídos do Bulbapedia;
- `pandasSerebii.py`: Tratamento dos dados extraídos do Serebii.

A partir do Terminal, execute os scrappers a partir dos comandos `scrapy runspider bulbapediaScrapper.py` e `scrapy runspider serebiScrapper.py`. Os processos podem demorar um pouco para finalizar, pois estamos lidando com uma base de dados com mais de 800 dados.

Ao final da execução, haverão 3 arquivos no formato json na pasta, `pokemons_bulbapedia.json` gerado pelo primeiro scrapper, e `pokemons_geral_serebii.json` e `pokemons_dano_fraqueza_serebii.json` gerados pelo segundo scrapper, respectivamente.

Após isso, deve-se executar o arquivo `main.py`, para que as informações dos arquivos json sejam tratadas - fazendo uso do conteúdo dos arquivos `pandasBulbapedia.py` e `pandasSerebii.py`. Ao final da execução, o arquivo `pokemonData.csv` terá sido gerado.
