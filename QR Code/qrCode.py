import pandas as pd
import qrcode
import csv
df = pd.read_csv(r'/home/narayanj/Practice/THAR/StudentsData/student-dataset.csv')
dataList1= df["id"].tolist()
dataList2= df["name"].tolist()
dataList3= df["nationality"].tolist()
DataList =  list(zip(dataList1, dataList2, dataList3))

for i in DataList:
    img = qrcode.make(i)
    img.save(f"qrcode_{i}.png")


