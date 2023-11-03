# import pandas as pd
# import qrcode
# import csv
# df = pd.read_csv(r'/home/narayanj/Practice/THAR/StudentsData/DATA1.csv')
# # dataList1= df["ID"].tolist()
# dataList2= df["NAME"].tolist()
# dataList3= df["CITY"].tolist()
# dataList4= df["UNIVERSITY"].tolist()
# dataList5= df["STAY REQ"].tolist()
# dataList6= df["PRO NITE"].tolist()
# dataList7= df["STAND ALONE EVENTS"].tolist()
# dataList8= df["GROUP EVENTS"].tolist()
# dataList9= df["CONTACT NO."].tolist()
# # DataList =  list(zip(dataList1, dataList2, dataList3, dataList4, dataList5, dataList6, dataList7, dataList8, dataList9))
# DataList =  list(zip(dataList2, dataList3, dataList4, dataList5, dataList6, dataList7, dataList8, dataList9))

# for i in DataList:
#     img = qrcode.make(i)
#     name = list(i)[0]
#     img.save(f"{name}")

import pandas as pd
import qrcode


class studentsData:
    def __init__(self, datafile):
        self.df = pd.read_csv(datafile)
        self.dataList2 = self.df["NAME"].tolist()
        self.dataList3 = self.df["CITY"].tolist()
        self.dataList4 = self.df["UNIVERSITY"].tolist()
        self.dataList5 = self.df["STAY REQ"].tolist()
        self.dataList6 = self.df["PRO NITE"].tolist()
        self.dataList7 = self.df["STAND ALONE EVENTS"].tolist()
        self.dataList8 = self.df["GROUP EVENTS"].tolist()
        self.dataList9 = self.df["CONTACT NO."].tolist()

    def genQRcode(self):
        data_list = list(zip(self.dataList2, self.dataList3, 
                             self.dataList4, self.dataList5, 
                             self.dataList6, self.dataList7, 
                             self.dataList8, self.dataList9))
                             
        for data in data_list:
            img = qrcode.make(data)
            name = data[0]
            img.save(f"{name}")

if __name__ == "__main__":
    data_file_path = '/home/narayanj/Practice/THAR/StudentsData/DATA1.csv'
    student_data = studentsData(data_file_path)
    student_data.genQRcode()
