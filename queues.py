from pcb import Pcb

class ReadyQueue:
    # Constructor
    def __init__(self):
        self.queuing_list:list[Pcb] = []
    
    # Adds new process at the back of the queue.
    def addProcess(self, newProcess:Pcb):
        self.queuing_list.append(newProcess)
    
    # Pops the first process of the queue.
    def removeFirstProcess(self) -> Pcb | None:
        if self.queuing_list:
            self.queuing_list[0].changeState(Pcb.RUNNING)
            return self.queuing_list.pop(0)
        else:
            print("No process found.")

    # Getters
    def getQueueList(self):
        return self.queuing_list
    
    # Checks if the list is empty
    def isEmpty(self):
        if len(self.queuing_list) == 0:
            return True
        else:
            return False

