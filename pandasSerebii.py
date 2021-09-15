from numpy.core.numeric import NaN
import pandas as pd

# Comando shell
# python3 pandasSerebii.py

def treatSerebiiData():
  general = pd.read_json('pokemons_geral_serebii.json')
  damageData = pd.read_json('pokemons_dano_fraqueza_serebii.json')

  ## -- Fazendo merge do dano por tipo num unico dataFrame -- ##
  goodInfo = pd.merge(general, damageData, left_on="Nome", right_on="Nome")

  ## -- Tratando os números -- ##
  # Tirando o # e colocando None em valores invalidos
  goodInfo['Num'] = goodInfo['Num'].str.replace('#', '')
  goodInfo['Num'] = goodInfo['Num'].replace('TBD', None)
  # Transformando em Int
  goodInfo['Num'] = goodInfo['Num'].astype(int)


  ## -- Tratando a evolução -- ##

  # Capturando informação da evolução
  goodInfo['proxEvol'] = goodInfo['proxEvol'].str.findall('art\/\d{3}\.png')
  # Removendo linhas que contem evolução invalida
  goodInfo = goodInfo[goodInfo['proxEvol'].notna()]

  # Tranformando as evoluções em lista
  ocurrences = pd.DataFrame(goodInfo.proxEvol.tolist(), index=goodInfo.index)

  # Removendo caracteres indesejaveis
  for col in ocurrences:
    ocurrences[col] = ocurrences[col].str.replace(".png", "")
    ocurrences[col] = ocurrences[col].str.replace("art/", "")

  # Remove valores None e a evolução que é o próprio pokemon.
  values = []
  indices = list(goodInfo['Num'])
  for i, col in zip(indices, ocurrences.values.tolist()):
      line = []
      for evol in col:
          if evol is not None and int(evol) > i:
            line.append(int(evol))
      values.append(line)
  goodInfo['proxEvol'] = values

  # Drop coluna Num
  # Não é necessaria
  goodInfo.drop(['Num'], axis=1, inplace=True)

  return goodInfo