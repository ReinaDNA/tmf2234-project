from pcb import Pcb
from queues import ReadyQueue
from CPU import CPU

TIME_QUANTUM = 3

def processChecker(time, job_list:list[Pcb]) -> ReadyQueue:
    arrived_jobs = ReadyQueue()
    if job_list:
        for job in job_list:
            if job.getArrivalTime() <= time:
                arrived_jobs.addProcess(job)
        for job in arrived_jobs.getQueueList():
            job_list.remove(job)

    return arrived_jobs

def main():
    #Universal clock timer
    time = 0
    job_list: list[Pcb] = []
    #Generate 100 dummy data for simulation.
    for i in range(100):
        job_list.append(Pcb(i+1))
    cpu = CPU(TIME_QUANTUM)
    available_jobs = processChecker(time, job_list)
    if available_jobs and cpu.checkIsIdle():
        cpu.fetchNextProcess(available_jobs)
        processing_time = cpu.executeProcess()
        time = time + processing_time
    
    print(f"The time now is {time}ms")


      
    


main()
