
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats



arry1 = np.random.randn(100000, 1)
print(arry1)
# draw a histogram

sns.displot(arry1, bins=50, kde=True)
plt.show()


