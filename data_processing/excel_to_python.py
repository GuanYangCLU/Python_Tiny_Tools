import pandas as pd

dataFrame = pd.read_excel (r'pm.xlsx', header=None)

arr = dataFrame.values.tolist()

print(arr)