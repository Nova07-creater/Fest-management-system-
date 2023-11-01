#  So we do have 2 kinds of events 

#  1) Stand Alone events including: "Gokarting", "Robo War" & "RC Nitro"
#  2) Group Events



# class Events: 

#     def __init__(self):
#         print("Greetings Buddy, The events are as follows: ")
#     StandAlone = ['Go-Kart', 'Robo War', 'RC Nitro', 'MUN']
#     GroupEvents = ['Goggle Hunters', 'Creo 3D', 'Dark Room']

#     def getevents(self):
#         global StandAlone, GroupEvents
        
#         print("Our Stand Alone Events: \n")
#         for i in StandAlone:
#             print(i)
#         print("Our Group Events: \n")
#         for i in GroupEvents:
#             print(i)

# participant = Events()

# participant.getevents()

StandAlone = ['Go-Kart', 'Robo War', 'RC Nitro', 'MUN'] 
GroupEvents = ['Goggle Hunters', 'Creo 3D', 'Dark Room']
class Events:
    def __init__(self):
       print("Greetings Buddy, We are organising both Stand-Alone and Group events\n")

    def getevents(self):  
        print('Our Stand Alone events are: \n')
        for i in StandAlone:
            print (i)
        print('\n')
        print('Our Group events are: \n')
        for i in GroupEvents:
            print (i)
participant = Events()
participant.getevents()

