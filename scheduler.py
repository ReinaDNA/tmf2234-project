from pcb import Pcb
from queues import ReadyQueue
class Scheduler:
    def __init__(self, available_jobs):
        self.ready_queue = ReadyQueue()
        self.available_jobs: list[Pcb] = available_jobs

    def filterAvailableProcess(self, time):
        not_ready_jobs: list[Pcb] = []
        if self.available_jobs:
            for job in self.available_jobs:
                if job.getArrivalTime() <= time:
                    print(f"Job {job.getProgramNumber()} arrived at {job.getArrivalTime()}")
                    self.ready_queue.addProcess(job)
                    print(f"Job {job.getProgramNumber()} added to ready queue")
                else:
                    not_ready_jobs.append(job)
            self.available_jobs = not_ready_jobs
            return self.ready_queue.getQueueList()
        else:
            print("No available jobs to schedule.")
    
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
