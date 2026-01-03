from pcb import Pcb
from CPU import CPU
from scheduler import Scheduler
from metrics import Metrics

SMALL_TIME_QUANTUM = 3
MEDIUM_TIME_QUANTUM = 10
LARGE_TIME_QUANTUM = 25
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
    process_list: list[Pcb] = []
    for i in range(100):
        new_process = Pcb(i+1)
        process_list.append(new_process)
    sortProcessByArrivalTime(process_list)
    return process_list

def roundRobin(time_quantum):
    #Universal clock timer
    time = 0
    process_list = dummyGenerator()
    metrics = Metrics()
    cpu = CPU(time_quantum)
    scheduler = Scheduler(process_list)
    while not (scheduler.ready_queue.isEmpty() and len(scheduler.getAvailableProcessList()) == 0 and cpu.checkIsIdle()):
        available_process = scheduler.filterAvailableProcess(time)
        if available_process and cpu.checkIsIdle():
            cpu.fetchNextProcess(scheduler)
            processing_time = cpu.executeProcess()
            time = time + processing_time
            available_process = scheduler.filterAvailableProcess(time)
            executed_process = scheduler.checkExecutedProcess(cpu.getCurrentProcess(), time)
            time = time + CONTEXT_SWITCH # A context switch occurs after the executeProcess() function.
            metrics.countContextSwitch()
            if executed_process:
                metrics.addCompletedProcess(executed_process)
                # print(f"Program #{cpu.current_process.getProgramNumber()} completed.")
            else:
                # print(f"Program #{cpu.current_process.getProgramNumber()} preempted.")
                pass
        else:
            # print("Don't have jobs available, forwarding time...")
            time = time + 1

        # print(f"The time now is {time}ms")

    # metrics.calculateMetrics()
    metrics.displaySystemMetrics()

def main():
    choice= input("Enter 1 for small time quantum, 2 for medium time quantum, 3 for large time quantum: ")
    if choice == "1":
        roundRobin(SMALL_TIME_QUANTUM)
    elif choice == "2":
        roundRobin(MEDIUM_TIME_QUANTUM)
    elif choice == "3":
        roundRobin(LARGE_TIME_QUANTUM)
    else:
        print("Invalid choice.")

main()
