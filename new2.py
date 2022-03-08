import pandas as pd
import seaborn as sns
import numpy as np
df=pd.Data({'a':['Airtime','Send Money','WithDraw Money'] ,'b':[50,100,150]})

sns.barplot(df['a'],df['b'], palette='Blues_d')
