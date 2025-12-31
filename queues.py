from pcb import Pcb

class ReadyQueue:
    def __init__(self):
        self.queuing_list = []
        
    def addProcess(self, newProcess:Pcb):
        self.queuing_list.append(newProcess)

    def fetchNextProcess(self):
        if self.queuing_list:
            return self.queuing_list.pop(0)
        else:
            print("No process found.")
            
    def getQueueList(self):
        return self.queuing_list
    
