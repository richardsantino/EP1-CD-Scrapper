from numpy.core.numeric import NaN
import pandas as pd

def treatBulbapediaData():
  #lê 'pokemons_bulpapedia.json' como pandas data
  pokemons_data = pd.read_json('pokemons_bulbapedia.json')
  pokemons_data.sort_values(by=['Num'], inplace=True)

  ### ['Num'] tratamento ###

  #remove "#" de 'Num' 
  pokemons_data['Num'] = pokemons_data['Num'].str.replace('#','')
  #deleta linhas que contem campos com None
  pokemons_data = pokemons_data[pokemons_data['Num'].notna()]
  #converte a coluna 'Num' para int
  pokemons_data['Num'] = pokemons_data['Num'].astype(int)

  ###['TamM']/['PesoLb']/['PesoKg'] tratamento ###

  #remove caracteres indesejaveis/seta como NaN dados invalidos
  pokemons_data['TamM'] = pokemons_data['TamM'].str.replace(' m\n','')
  pokemons_data['TamM'] = pokemons_data['TamM'].replace({"[[|": NaN})
  pokemons_data['PesoLb'] = pokemons_data['PesoLb'].str.replace(' lbs.\n','')
  pokemons_data['PesoKg'] = pokemons_data['PesoKg'].str.replace(' kg\n','')

  #converte para float
  pokemons_data['TamM'] = pokemons_data['TamM'].astype(float)
  pokemons_data['PesoLb'] = pokemons_data['PesoLb'].astype(float)
  pokemons_data['PesoKg'] = pokemons_data['PesoKg'].astype(float)

  ### ['Cor'] tratamento ###

  pokemons_data['Cor'] = pokemons_data['Cor'].str.replace("\n",'')

  ## ['Tipos'] tratamento ###

  ## separando ['Tipos'] em duas colunas(['tipo1', 'tipo2'])
  pokemons_data[['tipo1', 'tipo2']] = pd.DataFrame(pokemons_data.Tipos.tolist(), index=pokemons_data.index)
  pokemons_data.drop(['Tipos'], axis=1, inplace=True)

  ## trocando "Unknown" para None
  pokemons_data['tipo2'] = pokemons_data['tipo2'].replace({"Unknown": None})

  return pokemons_data