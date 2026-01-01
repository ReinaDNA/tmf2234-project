from pcb import Pcb

class ReadyQueue:
    def __init__(self):
        self.queuing_list:list[Pcb] = []
        
    def addProcess(self, newProcess:Pcb):
        self.queuing_list.append(newProcess)
   
    def removeFirstProcess(self) -> Pcb | None:
        if self.queuing_list:
            self.queuing_list[0].changeState(Pcb.RUNNING)
            return self.queuing_list.pop(0)
        else:
            print("No process found.")

    def getQueueList(self):
        return self.queuing_list
    
class CompletedQueue:
    def __init__(self):
        self.completed_list: list[Pcb] = []

    def addProcess(self, newProcess:Pcb):
        self.completed_list.append(newProcess)