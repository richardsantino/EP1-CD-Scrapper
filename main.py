import pandas as pd
import pandasSerebii as pdSerebii
import pandasBulbapedia as pdBulba

dataBulbapedia = pdBulba.treatBulbapediaData()

dataSerebii = pdSerebii.treatSerebiiData()

data = pd.merge(dataBulbapedia, dataSerebii, left_on="Nome", right_on="Nome", how='left')

columnNames = ['Number', 'Name', 'Size(m)', 'Weight(lb)', 'Weight(kg)','PokedexColor', 'Type1', 'Type2', 'Evolution', 'NormalDamage', 'FireDamage', 'WaterDamage', 'ElectricDamage', 'GrassDamage', 'IceDamage', 'FightingDamage', 'PoisonDamage', 'GroundDamage', 'FlyingDamage', 'PsychcDamage', 'BugDamage', 'RockDamage', 'GhostDamage', 'DragonDamage', 'DarkDamage', 'SteelDamage', 'FairyDamage']

data.columns = columnNames

data.sort_values(by='Number', inplace=True)
data.set_index('Number', inplace=True)

data.to_csv('pokemonData.csv')

pokeData = pd.read_csv('pokemonData.csv')