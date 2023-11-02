import pandas as pd
import qrcode
import csv
df = pd.read_csv(r'/home/narayanj/Practice/THAR/StudentsData/DATA1.csv')
# dataList1= df["ID"].tolist()
dataList2= df["NAME"].tolist()
dataList3= df["CITY"].tolist()
dataList4= df["UNIVERSITY"].tolist()
dataList5= df["STAY REQ"].tolist()
dataList6= df["PRO NITE"].tolist()
dataList7= df["STAND ALONE EVENTS"].tolist()
dataList8= df["GROUP EVENTS"].tolist()
dataList9= df["CONTACT NO."].tolist()
# DataList =  list(zip(dataList1, dataList2, dataList3, dataList4, dataList5, dataList6, dataList7, dataList8, dataList9))
DataList =  list(zip(dataList2, dataList3, dataList4, dataList5, dataList6, dataList7, dataList8, dataList9))

for i in DataList:
    img = qrcode.make(i)
    name = list(i)[0]
    img.save(f"{name}")
