from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000, 200000, 3650),
                   np.random.normal(43000, 100000, 3650),
                   np.random.normal(43500, 140000, 3650),
                   np.random.normal(48000, 70000, 3650)],
                  index=[1992, 1993, 1994, 1995])

year_avg = df.mean(axis=1)
year_std = df.std(axis=1)
confidence = 0.95
yerr = year_std / np.sqrt(df.shape[1]) * \
    stats.t.ppf((1+confidence)/2.0, df.shape[1]-1)
# print(year_std)
# print(yerr)

plt.figure()

bars = plt.bar(range(df.shape[0]), year_avg,
               yerr=yerr, alpha=0.6, color='rgby')

threshold = 42000
plt.axhline(y=threshold, color='grey')

plt.xticks(range(df.shape[0]), ['1992', '1993', '1994', '1995'], alpha=0.8)
plt.title('Ferreira et al, 2014')

plt.show()
