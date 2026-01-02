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
                    print(f"Job {job.getProgramNumber()} arrived at {job.getArrivalTime()} and has a burst time of {job.getBurstTime()}")
                else:
                    not_ready_jobs.append(job)
            self.available_jobs = not_ready_jobs
            for process in new_ready_jobs:
                self.ready_queue.addProcess(process)
                # print(f"Job {process.getProgramNumber()} added to ready queue")   
        return self.ready_queue.getQueueList()
    
    def fetchNextProcess(self) -> Pcb | None:
        return self.ready_queue.removeFirstProcess()

    def checkAvailableProcesses(self):
        if self.available_jobs:
            return True
        else:
            return False        

    def checkExecutedProcess(self, process:Pcb):
        if process.getCurrentState() == Pcb.COMPLETED:
            return process
        else:
            self.ready_queue.addProcess(process)
            return None

    def isAvailableJobsEmpty(self):
        if len(self.available_jobs) == 0:
            return True
        else:
            return False
        
    def getAvailableProcessList(self):
        return self.available_jobs