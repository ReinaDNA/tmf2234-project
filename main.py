from pcb import Pcb
from CPU import CPU
from scheduler import Scheduler
TIME_QUANTUM = 3



def main():
    #Universal clock timer
    time = 0
    job_list: list[Pcb] = []
    #Generate 100 dummy data for simulation.
    for i in range(100):
        job_list.append(Pcb(i+1))
    cpu = CPU(TIME_QUANTUM)
    scheduler = Scheduler(job_list)
    available_jobs = scheduler.processChecker(time)
    if available_jobs and cpu.checkIsIdle():
        cpu.fetchNextProcess(available_jobs)
        processing_time = cpu.executeProcess()
        time = time + processing_time
    
    print(f"The time now is {time}ms")


      
    


main()
