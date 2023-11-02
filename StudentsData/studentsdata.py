import pandas as pd

data = pd.read_csv('/home/narayanj/Practice/THAR/StudentsData/student-dataset.csv')

data.drop(data.columns[4:16], axis=1, inplace= True)
print(data)