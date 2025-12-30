from random import randint

class Pcb:
    def __init__(self, number):
        self.program_number = number
        self.arrival_time = randint(0,100) #Program arrival times are randomly generated between 0 and 100ms.
        self.burst_time = randint(5,50) #Program burst times are randomly generated between 5 and 50ms.
        self.start_time = 0 #Time when the program starts getting processed.
        self.finish_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        
    def getProgramNumber(self):
        return self.program_number
            
    def getArrivalTime(self):
        return self.arrival_time
