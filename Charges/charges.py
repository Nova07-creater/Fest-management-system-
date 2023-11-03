
import pandas as pd

print("Greetings Folks, If you are a students of our campus you don't need to pay anything, Rest all of the guest participants have to pay accordingly!!!")

print('''\n Charges For the Registraions are as follows: 
      
          1) If you are our campus student then everything is free for you\n
          2) If You are outside student then you have to pay accordingly: \n
                    a) 50% Off on totals for Campus Ambassadors.add()
                    b) 10,000 INR for each Stand Alone Event.
                    c) 500 INR for 3 events. 
                    d) 100 INR more per event if you want to participate in more than 3 events.
                    e) 500 INR for stay at Campus hostels. 
                    f) 1500 INR extra charges for the Pro-Nites.''')
               



# df =  pd.read_csv(r'/home/narayanj/Practice/THAR/StudentsData/student-dataset.csv')


df = pd.read_csv(r'/home/narayanj/Practice/THAR/StudentsData/DATA1.csv')

campusAmbList= df["CAMPUS AMBASSADOR"].tolist()
# Camp = pd.read_csv(r'/home/narayanj/Practice/THAR/Campus Ambassador/thar_ca.csv')

for i in campusAmbList:
    if i == "TRUE":
        print("Hurray, You are Campus Ambassador, You got 50% off on your totals")
    else:
        print("Please proceed towards payment for your registration process")



#Here I have to check whether participant has paid or not using the CSV file

NumEventsparticipated = int(input('How many events you want to register? '))

if NumEventsparticipated == 3:
    print("Pay 500 INR for your registration \n")
if NumEventsparticipated <3:
    amount = NumEventsparticipated*100
    print(f'You need to pay {amount} INR for your registration \n')
if NumEventsparticipated>3:
    amount2 = (NumEventsparticipated-3)*100
    Total = amount2+500
    print(f'You need to pay {Total} INR for your registration')


