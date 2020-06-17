import pandas as pd
import re
poke = pd.read_csv('pokemon_data.txt',delimiter='\t')
#print(poke[['HP','Name']])
#print (poke.iloc[1:3])
#print(poke.iloc[1,4])

# for index, row in poke.iterrows():
#     print(index, row['Name'])

#print(poke.loc[poke['Type 1'] == "Plant"])

#print(poke.sort_values('Name', ascending = False))

#poke['Total'] = poke['HP'] + poke['Attack'] + poke['Defense']
#print(poke.head(5))


#poke = poke.drop(columns = ['Total'])


# poke['Total'] = poke.iloc[:, 4:9].sum(axis=1)
# print(poke.head(5))

# cols = list(poke.columns)
# poke = poke[cols[0:4] + [cols[-1]] + cols[4:12]]

# print(poke.head(5))

# poke.to_csv('modified.csv')

#poke.loc[(poke['Type 1'] == 'Grass') & (poke['Type 2'] == 'Poison')] 

#poke.loc[~poke['Name'].str.contains('Mega')]
#poke.loc[poke['Type 1'].str.contains('fire|grass', flags = re.I, regex= True)]
a = poke.loc[poke['Name'].str.contains('^pi[a-z]', flags = re.I, regex = True)]
print(a)