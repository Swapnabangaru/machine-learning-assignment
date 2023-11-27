


import pandas as pd
from scipy import stats as stats
from scipy.stats import chi2_contingency
from scipy.stats import chi2
custom= pd.read_csv("C:\\Users\\user\\Downloads\\Costomer+OrderForm.csv")
custom.head()

print(custom['Phillippines'].value_counts(),custom['Indonesia'].value_counts(),custom['Malta'].value_counts(),custom['India'].value_counts())

observed=([[271,267,269,280],[29,33,31,20]])
observed

stat, p, dof, expected = chi2_contingency([[271,267,269,280],[29,33,31,20]])
stat

p

print('dof=%d' % dof)
print(expected)

alpha = 0.05
prob=1-alpha
critical = chi2.ppf(prob, dof)
print('probability=%.3f, critical=%.3f, stat=%.3f' % (prob, critical, stat))
if abs(stat) >= critical:
	print('Dependent (reject H0),variables are related')
else:
	print('Independent (fail to reject H0), variables are not related')

print('significance=%.3f, p=%.3f' % (alpha, p))
if p <= alpha:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')

 