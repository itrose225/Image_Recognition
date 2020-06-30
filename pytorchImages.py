# import modules
import os
import numpy as np
import pandas as pd
from scipy.misc import imread
from sklearn.metrics import accuracy_score
#%matplotlib inline

seed = 5
rng = np.random.RandomState(seed)
print(rng)