'''
Created on Jun 22, 2017

@author: hdusr
'''
import pandas as pd
import numpy as np
import matplotlib
#this is a test comment

from matplotlib import pyplot as plt
import seaborn as sns

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()

df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                  columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
#df.plot();
plt.ion()
plt.plot(df)
plt.savefig('tweet_by_prg_language_2', format='png')
plt.show()
#plt.legend(loc='best')