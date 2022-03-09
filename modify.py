import pandas as pd

df = pd.read_csv('urbanization-census-tract-updated.csv', converters={'FIPS': lambda x: str(x)}) # add converters to keep leading zeros
df['total_pop'] = df.groupby(['FIPS'])['population'].transform('sum')
df.drop_duplicates(subset=['FIPS', 'total_pop'], keep="first", inplace=True)
df = df.drop(df.columns[[0, 1, 2]], axis=1)  # df.columns is zero-based pd.Index
df.to_csv('updated-census-tract.csv')