from pcb import Pcb
from queues import ReadyQueue
class Scheduler:
    def __init__(self, available_jobs):
        self.ready_queue = ReadyQueue()
        self.available_jobs: list[Pcb] = available_jobs

    def processChecker(self, time):
        if self.available_jobs:
            for i, job in enumerate(self.available_jobs):
                if job.getArrivalTime() <= time:
                    print(f"Job {job.getProgramNumber()} arrived at {job.getArrivalTime()}")
                    ready_job = self.available_jobs.pop(i)
                    self.ready_queue.addProcess(ready_job)
                    print(f"Job {job.getProgramNumber()} added to ready queue")
        return self.ready_queue