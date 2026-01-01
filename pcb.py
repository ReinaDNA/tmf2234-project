from random import randint

class Pcb:
    NEW = "New"
    READY = "Ready"
    RUNNING = "Running"
    COMPLETED = "Completed"
    def __init__(self, number):
        self.program_number = number
        self.arrival_time = randint(0,100) #Program arrival times are randomly generated between 0 and 100ms.
        self.burst_time = randint(5,50) #Program burst times are randomly generated between 5 and 50ms.
        self.start_time = 0 #Time when the program starts getting processed.
        self.finish_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.current_state = Pcb.NEW

    def getProgramNumber(self):
        return self.program_number
            
    def getArrivalTime(self):
        return self.arrival_time
    
    def getBurstTime(self):
        return self.burst_time

    def getCurrentState(self):
        return self.current_state
    
    def changeState(self, state):
        if state == Pcb.READY:
            self.current_state = Pcb.READY
        elif state == Pcb.RUNNING:
            self.current_state = Pcb.RUNNING
        elif state == Pcb.COMPLETED:
            self.current_state = Pcb.COMPLETED
        else:
            print("Error, invalid state.")
    
    def markAsComplete(self):
        self.burst_time = 0
        self.changeState(Pcb.COMPLETED)

    def setBurstTime(self, newBurst):
        self.burst_time = newBurst
        
