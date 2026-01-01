import pandas as pd

df = pd.DataFrame()
df['color'] = ['blue', 'red', 'yellow', 'green']
df['radius'] = [2,4,3,5]
print(df)

# Calcular una nueva columna de diametro multiplicando el radio por 2.
#df['diameter'] = df['radius'] * 2
#print(f'\n {df}')

# Calculos de columnas
#df['radius'].min()
#df['diameter'].sum()
#df['radius'].mean()

#df['color']

#df.iloc[0]
#df.iloc[1]
#df.iloc[-1]

#df.shape
#df.shape[0]
#df.shape[1]

layers = pd.read_csv('earth-layers.csv')
print(f'\n{layers}')
layers['thickness'].sum()
