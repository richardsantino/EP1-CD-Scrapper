import scrapy, json

class PokemonScrapper(scrapy.Spider):
  name = 'pokescrapper'
  domain = 'https://www.serebii.net'

  pokeInfo = []
  pokeDamage = []

  start_urls = ["https://www.serebii.net/pokemon/nationalpokedex.shtml"]
  
  def parse(self, response):
    pokes = response.css('main table tr')
    counter = 0
    for poke in pokes:
      pokemonURL = poke.css('td:nth-child(3)>a::attr(href)').get()
      if pokemonURL is not None:
        yield response.follow(self.domain + pokemonURL, self.parse_pokemon)
    
  def parse_pokedex(self, response):
    pokeURL = response.css('main> table tr td div .hubheader>a::attr(href)').get()
    yield response.follow(self.domain + pokeURL, self.parse_damage)
    
  # Pokedano por pokecada poketipo
  def parse_damage(self,response):
    url = response.request.url

    pokeName = response.css('#rbar>table:nth-child(4)>tr:nth-child(2) td::text').get()
    normal = ""
    fire = ""
    water = ""
    electric = ""
    grass = ""
    ice = ""
    fighting = ""
    poison = ""
    ground = ""
    flying = ""
    psychc = ""
    bug = ""
    rock = ""
    ghost = ""
    dragon = ""
    dark = ""
    steel = ""
    fairy = ""

    if 'pokedex-sm' in url:
      normal = response.css('main div>table:nth-child(7) tr:nth-child(3) td::text').get()

      fire = response.css('main div>table:nth-child(7) tr:nth-child(3) td:nth-child(2)::text').get()
        
      water = response.css('main div>table:nth-child(7) tr:nth-child(3) td:nth-child(3)::text').get()

      electric = response.css('main div>table:nth-child(7) tr:nth-child(3) td:nth-child(4)::text').get()

      grass = response.css('main div>table:nth-child(7) tr:nth-child(3) td:nth-child(5)::text').get()

      ice = response.css('main div>table:nth-child(7) tr:nth-child(3) td:nth-child(6)::text').get()

      fighting = response.css('main div>table:nth-child(7) tr:nth-child(3) td:nth-child(7)::text').get()

      poison = response.css('main div>table:nth-child(7) tr:nth-child(3) td:nth-child(8)::text').get()

      ground = response.css('main div>table:nth-child(7) tr:nth-child(3) td:nth-child(9)::text').get()

      flying = response.css('main div>table:nth-child(7) tr:nth-child(3) td:nth-child(10)::text').get()

      psychc = response.css('main div>table:nth-child(7) tr:nth-child(3) td:nth-child(11)::text').get()

      bug = response.css('main div>table:nth-child(7) tr:nth-child(3) td:nth-child(12)::text').get()

      rock = response.css('main div>table:nth-child(7) tr:nth-child(3) td:nth-child(13)::text').get()

      ghost = response.css('main div>table:nth-child(7) tr:nth-child(3) td:nth-child(14)::text').get()

      dragon = response.css('main div>table:nth-child(7) tr:nth-child(3) td:nth-child(15)::text').get()

      dark = response.css('main div>table:nth-child(7) tr:nth-child(3) td:nth-child(16)::text').get()

      steel = response.css('main div>table:nth-child(7) tr:nth-child(3) td:nth-child(17)::text').get()

      fairy = response.css('main div>table:nth-child(7) tr:nth-child(3) td:nth-child(18)::text').get()

    elif 'pokedex-swsh' in url:
      normal = response.css('table[style*="@media"]>tr:nth-child(3)>td::text').get()

      fire = response.css('table[style*="@media"]>tr:nth-child(3)>td:nth-child(2)::text').get()
        
      water = response.css('table[style*="@media"]>tr:nth-child(3)>td:nth-child(3)::text').get()

      electric = response.css('table[style*="@media"]>tr:nth-child(3)>td:nth-child(4)::text').get()

      grass = response.css('table[style*="@media"]>tr:nth-child(3)>td:nth-child(5)::text').get()

      ice = response.css('table[style*="@media"]>tr:nth-child(3)>td:nth-child(6)::text').get()

      fighting = response.css('table[style*="@media"]>tr:nth-child(3)>td:nth-child(7)::text').get()

      poison = response.css('table[style*="@media"]>tr:nth-child(3)>td:nth-child(8)::text').get()

      ground = response.css('table[style*="@media"]>tr:nth-child(3)>td:nth-child(9)::text').get()

      flying = response.css('table[style*="@media"]>tr:nth-child(3)>td:nth-child(10)::text').get()

      psychc = response.css('table[style*="@media"]>tr:nth-child(3)>td:nth-child(11)::text').get()

      bug = response.css('table[style*="@media"]>tr:nth-child(3)>td:nth-child(12)::text').get()

      rock = response.css('table[style*="@media"]>tr:nth-child(3)>td:nth-child(13)::text').get()

      ghost = response.css('table[style*="@media"]>tr:nth-child(3)>td:nth-child(14)::text').get()

      dragon = response.css('table[style*="@media"]>tr:nth-child(3)>td:nth-child(15)::text').get()

      dark = response.css('table[style*="@media"]>tr:nth-child(3)>td:nth-child(16)::text').get()

      steel = response.css('table[style*="@media"]>tr:nth-child(3)>td:nth-child(17)::text').get()

      fairy = response.css('table[style*="@media"]>tr:nth-child(3)>td:nth-child(18)::text').get()

    self.pokeDamage.append(
      {
        "Nome": pokeName,
        "Normal": normal,
        "Fire": fire,
        "Water": water,
        "Electric": electric,
        "Grass": grass,
        "Ice": ice,
        "Fighting": fighting,
        "Poison": poison,
        "Ground": ground,
        "Flying": flying,
        "Psychc": psychc,
        "Bug": bug,
        "Rock": rock,
        "Ghost": ghost,
        "Dragon": dragon,
        "Dark": dark,
        "Steel": steel,
        "Fairy": fairy
        
      }
    )

    with open('pokemons_dano_fraqueza_serebii.json', 'w') as json_file:
      json.dump(self.pokeDamage, json_file, indent = 2)

  def parse_pokemon(self, response):
    
    pokeNumber = ""
    pokeName = ""
    pokevolutionTable = ""

    if response.css('main>div:nth-child(2)>table:nth-child(4)').get() is not None:
      # Pokenumero
      pokeNumber = response.css('main>div:nth-child(2)>table:nth-child(4)>tr:nth-child(2)>td:nth-child(3)> table tr td:nth-child(2)::text').get()

      # Pokenome
      pokeName = response.css('main>div:nth-child(2)>table:nth-child(4)>tr:nth-child(2)>td:nth-child(2)> table tr td:nth-child(2)::text').get()

      # Pokevolução
      pokevolutionTable = response.css('.evochain').get()
    else:
      # Pokenumero
      pokeNumber = response.css('main div table tr:nth-child(2) td:nth-child(3) table tr td:nth-child(2)::text').get()

      # Pokenome
      pokeName = response.css('main div table tr:nth-child(2) td:nth-child(2) table tr td:nth-child(2)::text').get()

      # Pokevolução
      pokevolutionTable = response.css('.evochain').get()

    self.pokeInfo.append(
      {
        "Num": pokeNumber,
        "Nome": pokeName,
        "proxEvol": pokevolutionTable,
      }
    )

    with open('pokemons_geral_serebii.json', 'w') as json_file:
      json.dump(self.pokeInfo, json_file, indent = 2)

    yield response.follow(response.request.url, self.parse_pokedex, dont_filter = True)