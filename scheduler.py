from pcb import Pcb
from queues import ReadyQueue
class Scheduler:
    def __init__(self, available_jobs):
        self.ready_queue = ReadyQueue()
        self.available_jobs: list[Pcb] = available_jobs

    def processChecker(self, time):
        if self.available_jobs:
            for job in self.available_jobs:
                if job.getArrivalTime() <= time:
                    self.ready_queue.addProcess(job)
            for job in self.ready_queue.getQueueList():
                self.available_jobs.remove(job)
        return self.ready_queue