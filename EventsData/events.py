#  So we do have 2 kinds of events

#  1) Stand Alone events including: "Gokarting", "Robo War" & "RC Nitro"
#  2) Group Events

import pandas as pd
df = pd.read_csv(r'/home/narayanj/Practice/THAR/EventsData/events.csv')
GroupEvents = df['EVENT NAME'].tolist()
StandAlone = ['Go-Kart', 'Robo War', 'RC Nitro', 'MUN']


class Events:
    def __init__(self):
        print("Greetings Buddy, We are organising both Stand-Alone and Group events\n")

    def getevents(self):
        print('Our Stand Alone events are: \n')
        for i in StandAlone:
            print(i)
        print('\n')
        print('Our Group events are: \n')
        for i in GroupEvents:
            print(i, sep='\n')


NumGroup = int(input("Number of events (Group Events)you are interested in? "))
Groupevelist = []
for i in range(0, NumGroup):
    event = input("Which event you want to participate? ")
    Groupevelist.append(event)
print('\n')
print(f'So you have registered in {NumGroup} events and these are: \n')
count = 1
for i in Groupevelist:
    print(count, i)
    count += 1
StandEvelist =[]
NumStand = int(input('Number of Stand Alone events you are interested in?'))

for i in range(0, NumStand):
    event = input('Which event you want to  participate? ')
    StandEvelist.append(event)
print('\n')
print(f'So you have registered in {NumStand} events and these are: \n')
Count = 1
for i in StandEvelist:
    print(count, i)
    Count += 1
participant = Events()
participant.getevents()
