import pandas as pd
import numpy as np
import datetime

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df.describe()
print(df)

data = [(53654, '04f1', 33, datetime.datetime(1970, 1, 1, 21, 14, 20)), (46384, '06b0', 94, datetime.datetime(1970, 1, 1, 20, 39, 25))]

print('-----------')
df1 = pd.DataFrame(data)
# print(df1['A'])
print(df1)