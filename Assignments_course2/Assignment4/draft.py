import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-colorblind')
np.random.seed(1234)
v1 = pd.Series(np.random.normal(0, 10, 1000), name='v1')
v2 = pd.Series(2*v1 + np.random.normal(60, 15, 1000), name='v2')

plt.figure()
# plt.hist(v1, alpha=0.7, bins=np.arange(-50, 150, 5), label='v1')
# plt.hist(v2, alpha=0.7, bins=np.arange(-20, 150, 5), label='v2')
# plt.legend()
plt.hist([v1, v2], histtype='barstacked', normed=True)
v3 = np.concatenate((v1, v2))
sns.kdeplot(v3)
plt.show()
