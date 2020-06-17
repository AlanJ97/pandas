import pandas as pd

poke = pd.read_csv('pokemon_data.txt',delimiter='\t')
#print(poke[['HP','Name']])
#print (poke.iloc[1:3])
print(poke.iloc[1,4])

