from pcb import Pcb
from CPU import CPU
from scheduler import Scheduler
from metrics import Metrics

TIME_QUANTUM = 3
CONTEXT_SWITCH = 1

def sortProcessByArrivalTime(process_list:list[Pcb]):
    #Simple bubble sort function 
    #Sorting the processes by arrival time as it is randomly generated per process.
    n = len(process_list)
    for i in range(n):
        swapped = False
        for process in range(0, n-i-1):
            if process_list[process].getArrivalTime() > process_list[process+1].getArrivalTime():
                process_list[process], process_list[process+1] = process_list[process+1], process_list[process]
                swapped = True
        if not swapped:
            break

#Generate 100 dummy data for simulation.
def dummyGenerator() -> list[Pcb] | None:
    job_list: list[Pcb] = []
    
    job_list.append(Pcb(1, 5, 15))
    job_list.append(Pcb(2, 8, 21))
    job_list.append(Pcb(3, 14, 23))
    job_list.append(Pcb(4, 9, 27))
    job_list.append(Pcb(5, 30, 44))
    sortProcessByArrivalTime(job_list)
    return job_list

def main():
    #Universal clock timer
    time = 0
    job_list = dummyGenerator()
    metrics = Metrics()
    cpu = CPU(TIME_QUANTUM)
    scheduler = Scheduler(job_list)
    while not (scheduler.ready_queue.isEmpty() and len(scheduler.getAvailableProcessList()) == 0):
        available_job = scheduler.filterAvailableProcess(time)
        if available_job and cpu.checkIsIdle():
            cpu.fetchNextProcess(scheduler)
            processing_time = cpu.executeProcess()
            time = time + processing_time
            available_job = scheduler.filterAvailableProcess(time)
            executed_process = scheduler.checkExecutedProcess(cpu.getCurrentProcess(), time)
            time = time + CONTEXT_SWITCH # A context switch occurs after the executeProcess() function.
            metrics.countContextSwitch()
            if executed_process:
                metrics.addCompletedProcess(executed_process)
                print(f"Program #{cpu.current_process.getProgramNumber()} completed.")
            else:
                print(f"Program #{cpu.current_process.getProgramNumber()} preempted, next loop...")
        else:
            print("Don't have jobs available, forwarding time...")
            time = time + 1

        print(f"The time now is {time}ms")
        # for process in scheduler.ready_queue.getQueueList():
        #     print(process.getProgramNumber())
    metrics.calculateMetrics()
    print(f"Average Turnaround Time: {metrics.calculateAverageTurnaroundTime()}ms")
    print(f"Average Waiting Time: {metrics.calculateAverageWaitingTime()}ms")
    print(f"Total Number of Context Switches: {metrics.getContextSwitchCount()}")
    print(f"Total CPU Overhead caused By Context Switching: {metrics.getCPUOverhead()}ms")

main()
