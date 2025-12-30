from pcb import Pcb
from queues import ReadyQueue
class CPU:
    BUSY = "Busy"
    IDLE = "Idle"

    def __init__(self, quantum):
        self.time_quantum = quantum
        self.current_process : Pcb = None
        self.state = CPU.IDLE

    def fetchNextProcess(self, queue:ReadyQueue):
        self.current_process = queue.fetchNextProcess()
    
    def checkIsIdle(self):
        if self.state == CPU.IDLE:
            return True
        else:
            return False
        
    def executeProcess(self):
        if self.current_process is not None:
            self.state = CPU.BUSY
            self.current_process.changeState(Pcb.RUNNING)
            required_time = self.current_process.getBurstTime()
            if required_time < self.time_quantum:
                self.current_process.markAsComplete()
                self.state = CPU.IDLE
                return required_time
            else:
                remaining_burst_time = self.current_process.getBurstTime() - self.time_quantum
                self.current_process.setBurstTime(remaining_burst_time)
                self.current_process.changeState(Pcb.READY)
                return self.time_quantum
        else:
            print("Error, CPU does not hold a process.")