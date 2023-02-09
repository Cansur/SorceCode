import os
import pandas as pd

f_path = r'C:\Users\tjswo\OneDrive\바탕 화면\이선재\SorceCode\test.py'
f_name = "data_tmp.csv"

df3 = pd.DataFrame({'B': ['a', 'c', 'b', 'd'],
                    'C': [3, 6, 9, 1],
                    'D': ['b', 'b', 'e', 'a']})
# f = open('hh.txt','w')
# f.write(f_path)
# f.close()
# line = f.readline()
# print(line)
df3.to_csv(index=False)