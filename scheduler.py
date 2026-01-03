from pcb import Pcb
from queues import ReadyQueue

class Scheduler:
    # Constructor
    def __init__(self, available_process):
        self.ready_queue = ReadyQueue()
        self.available_processes: list[Pcb] = available_process

    # Checks the current time for process arrivals
    def filterAvailableProcess(self, time):
        not_ready_process: list[Pcb] = []
        if self.available_processes:
            for process in self.available_processes:
                if process.getArrivalTime() <= time:
                    # Inserts the processes into the ready queue.
                    process.changeState(Pcb.READY)
                    self.ready_queue.addProcess(process)
                else:
                    # Processes that have not arrived are placed into another list
                    not_ready_process.append(process)
            # Copy the not arrived processes list back to the original list of proceses
            # This method is used to avoid list manipulation during iteration of a loop.
            self.available_processes = not_ready_process        
        return self.ready_queue.getQueueList() # Returns the ready queue to the caller.
    
    # Sends the next process in the ready queue to the CPU.
    def fetchNextProcess(self) -> Pcb | None:
        return self.ready_queue.removeFirstProcess()     

    # Checks if a PCB is completed.
    def checkExecutedProcess(self, process:Pcb, time):
        if process.getCurrentState() == Pcb.COMPLETED:
            process.setFinishTime(time)
            return process
        else:
            # Requeues the PCB in the ready queue if not completed.
            self.ready_queue.addProcess(process)
            return None
        
    # Getter
    def getAvailableProcessList(self):
        return self.available_processes