import numpy as np                   # for multi-dimensional containers 
import pandas as pd                  # for DataFrames

df = pd.read_csv('pokemon.csv')

variable = df.loc[df["Sp_Atk"],'Name']

print( variable )
