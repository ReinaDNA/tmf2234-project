from random import randint

class Pcb:
    # Constants used to define states
    NEW = "New"
    READY = "Ready"
    RUNNING = "Running"
    COMPLETED = "Completed"

    # Constructor
    def __init__(self, number):
        self.program_number = number
        self.arrival_time = randint(0,100) # Program arrival times are randomly generated between 0 and 100ms.
        self.burst_time = randint(5,50) # Program burst times are randomly generated between 5 and 50ms.
        self.initial_burst_time = self.burst_time # Variable used to calculate waiting time afterwards. 
        self.finish_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.current_state = Pcb.NEW

    # Mark this PCB as completed.
    def markAsComplete(self):
        self.burst_time = 0
        self.changeState(Pcb.COMPLETED)

    # Change the state of the PCB
    def changeState(self, state):
        if state == Pcb.READY:
            self.current_state = Pcb.READY
        elif state == Pcb.RUNNING:
            self.current_state = Pcb.RUNNING
        elif state == Pcb.COMPLETED:
            self.current_state = Pcb.COMPLETED
        else:
            print("Error, invalid state.")

    # Getters
    def getProgramNumber(self):
        return self.program_number
            
    def getArrivalTime(self):
        return self.arrival_time
    
    def getBurstTime(self):
        return self.burst_time

    def getCurrentState(self):
        return self.current_state
    
    def getFinishTime(self):
        return self.finish_time    
    
    def getTurnaroundTime(self):
        return self.turnaround_time  

    def getWaitingTime(self):
        return self.waiting_time  

    # Setters
    def setBurstTime(self, newBurst):
        self.burst_time = newBurst
        
    def setFinishTime(self, finish):
        self.finish_time = finish

    def setTurnaroundTime(self):
        self.turnaround_time = self.finish_time - self.arrival_time
    
    def setWaitingTime(self):
        self.waiting_time = self.turnaround_time - self.initial_burst_time