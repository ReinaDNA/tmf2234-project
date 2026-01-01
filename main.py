from pcb import Pcb
from CPU import CPU
from queues import CompletedQueue
from scheduler import Scheduler
TIME_QUANTUM = 3
#Generate 100 dummy data for simulation.
def dummyGenerator() -> list[Pcb] | None:
    job_list: list[Pcb] = []
    for i in range(100):
        job_list.append(Pcb(i+1))
    return job_list

def main():
    #Universal clock timer
    time = 0
    job_list = dummyGenerator()
    completed = CompletedQueue()
    cpu = CPU(TIME_QUANTUM)
    scheduler = Scheduler(job_list)
    available_jobs = scheduler.filterAvailableProcess(time)
    if available_jobs and cpu.checkIsIdle():
        cpu.fetchNextProcess(scheduler)
        processing_time = cpu.executeProcess()
        time = time + processing_time
        executed_process = scheduler.checkExecutedProcess(cpu.getCurrentProcess())
        if executed_process:
            completed.addProcess(executed_process)
        else:
            print("Execution completed, next loop...")
    else:
        print("Unable to execute Process.")

    print(f"The time now is {time}ms")


      
    


main()
