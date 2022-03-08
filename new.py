import numpy as np
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 5):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
sinplot()
#plt.show()

def data_info():
    dataset = pd.read_csv('data.csv')
   # df = sb.load_dataset(dataset)
    sb.displot(df['Transaction'] , kde = False)
plt.show()  