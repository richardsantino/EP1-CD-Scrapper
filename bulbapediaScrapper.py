import scrapy, json

class PokemonScrapper(scrapy.Spider):
  pokeInfo = []
  name = 'pokemon_scrapper'
  domain = 'https://bulbapedia.bulbagarden.net'

  start_urls = ["https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"]

  def parse(self, response):
    pokemons = response.css('tr')
    print(len(pokemons))
    for pokemon in pokemons:

      pokemon_url = pokemon.css('td>a::attr(href)').get()
      if pokemon_url is not None:
        yield response.follow(self.domain + pokemon_url, self.parse_pokemon)

  def parse_pokemon(self, response):
    # Pokenumero
    pokeNumber = response.css('.mw-parser-output>table:nth-child(2)>tbody tr td>table tbody tr th big big a span::text').get()

    # Pokenome
    pokeName = response.css('td big big b::text').get()

    # Poketamanho
    pokeHeightM = response.css('.mw-parser-output>table:nth-child(2)>tbody>tr:nth-child(6)>td tbody tr td:nth-child(2)::text').get()

    # Pokepeso
    pokeWeightLb = response.css('.mw-parser-output>table:nth-child(2)>tbody>tr:nth-child(6)>td:nth-child(2)>table tbody tr td::text').get()
    pokeWeightKg = response.css('.mw-parser-output>table:nth-child(2)>tbody>tr:nth-child(6)>td:nth-child(2)>table tbody tr td:nth-child(2)::text').get()

    # Poketipo
    pokeType1 = response.css('.mw-parser-output>table:nth-child(2)>tbody>tr:nth-child(2)> td>table tbody tr td> table tbody tr>td a span b::text').get()
    pokeType2 = response.css('.mw-parser-output>table:nth-child(2)>tbody>tr:nth-child(2)> td>table tbody tr td> table tbody tr>td:nth-child(2) a span b::text').get()

    # Pokecor na pokedex
    pokeColor = response.css('.mw-parser-output>table:nth-child(2)>tbody>tr:nth-child(11)>td>table tbody tr td::text').get()

    self.pokeInfo.append(
      {
        "Num": pokeNumber,
        "Nome": pokeName,
        "TamM": pokeHeightM,
        "PesoLb": pokeWeightLb,
        "PesoKg": pokeWeightKg,
        "Cor": pokeColor,
        "Tipos": [pokeType1, pokeType2]
      }
    )

    with open('pokemons_bulbapedia.json', 'w') as json_file:
      json.dump(self.pokeInfo, json_file, indent = 2)