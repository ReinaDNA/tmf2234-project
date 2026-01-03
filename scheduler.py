from pcb import Pcb
from queues import ReadyQueue
class Scheduler:
    def __init__(self, available_jobs):
        self.ready_queue = ReadyQueue()
        self.available_jobs: list[Pcb] = available_jobs

    def filterAvailableProcess(self, time):
        not_ready_jobs: list[Pcb] = []
        new_ready_jobs: list[Pcb] = []
        if self.available_jobs:
            for job in self.available_jobs:
                if job.getArrivalTime() <= time:
                    new_ready_jobs.append(job)
                else:
                    not_ready_jobs.append(job)
            self.available_jobs = not_ready_jobs
            for process in new_ready_jobs:
                process.changeState(Pcb.READY)
                self.ready_queue.addProcess(process)
        return self.ready_queue.getQueueList()
    
    def fetchNextProcess(self) -> Pcb | None:
        return self.ready_queue.removeFirstProcess()     

    def checkExecutedProcess(self, process:Pcb, time):
        if process.getCurrentState() == Pcb.COMPLETED:
            process.setFinishTime(time)
            return process
        else:
            self.ready_queue.addProcess(process)
            return None
        
    def getAvailableProcessList(self):
        return self.available_jobs