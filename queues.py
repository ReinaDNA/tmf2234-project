from pcb import Pcb

class ReadyQueue:
    def __init__(self):
        self.queuing_list = []
        
    def addProcess(self, newProcess:Pcb):
        self.queuing_list.append(newProcess)

    def fetchNextProcess(self):
        return self.queuing_list.pop(0)
    
    def getQueueList(self):
        return self.queuing_list
    
