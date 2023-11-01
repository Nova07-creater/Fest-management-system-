# Charges for University campus participants 

        # No charges for campus students.

# Charges for participants who are not campus students

        # Chargees for All the 3 Pro-nites is 1500 INR
        # Charges for events are as follows: 
                # Can register in 3 events for 500 INR
                # After 3 events participant needs to pay 100 INR per event.
import pandas as pd

print("Greetings Folks, If you are a students of our campus you don't need to pay anything, Rest all of the guest participants have to pay accordingly!!!")

df =  pd.read_csv(r'/home/narayanj/Practice/THAR/StudentsData/student-dataset.csv')
# print(df)


Nationality = df["nationality"].tolist()
# print(Nationality)


# for i in Nationality:
#     if i == 'United States of America':
#         print('You don\'t need to pay anything')
#     else: 
#         print('Buddy, You have to pay the specific charges')

UniversityName = input("Your University name? ")

for uni in Nationality:
    if uni == UniversityName:
        print("Hurray, You may register for free!! \n")
    else:
        print("Buddy, You have to go through payment process to register")
        