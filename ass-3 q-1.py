import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
# Load the dataset
data=pd.read_csv("C:\\Users\\user\\Downloads\\Cutlets.csv")
data.head()

unitA=pd.Series(data.iloc[:,0])
unitA

unitB=pd.Series(data.iloc[:,1])
unitB



# 2-sample 2-tail ttest:   stats.ttest_ind(array1,array2)     # ind -> independent samples
p_value=stats.ttest_ind(unitA,unitB)
p_value


p_value[1]     # 2-tail probability 

# compare p_value with α = 0.05 (At 5% significance level)

