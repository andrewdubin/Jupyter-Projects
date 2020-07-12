import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv('Unemployment/unemployment.csv')
df.columns = ['Date','Number']

df.head()
