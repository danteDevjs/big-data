import pandas as pd



pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv('./dataset/seguridad_sucio.csv')

  
print(df.isnull().mean() * 100 )



