

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
# load the dataset
data=pd.read_csv("C:\\Users\\user\\Downloads\\LabTAT.csv")
data.head()

# Anova ftest statistics: stats.f_oneway(column-1,column-2,column-3,column-4)
p_value=stats.f_oneway(data.iloc[:,0],data.iloc[:,1],data.iloc[:,2],data.iloc[:,3])
p_value

p_value[1]  # compare it with α = 0.05
