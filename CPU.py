from pcb import Pcb
from queues import ReadyQueue
class CPU:
    def __init__(self, quantum):
        self.time_quantum = quantum
        self.current_process : Pcb = None

    def fetchNextProcess(self, queue:ReadyQueue):
        self.current_process = queue.fetchNextProcess()
    
    def executeProcess(self):
        if self.current_process is not None:
            self.current_process.changeState(Pcb.RUNNING)
            if self.current_process.getBurstTime() < self.time_quantum:
                self.current_process.changeState(Pcb.COMPLETED)
            else:
                remaining_burst_time = self.current_process.getBurstTime() - self.time_quantum
                self.current_process.setBurstTime(remaining_burst_time)
                self.current_process.changeState(Pcb.READY)
        else:
            print("Error, CPU does not hold a process.")