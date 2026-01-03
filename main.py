from pcb import Pcb
from CPU import CPU
from scheduler import Scheduler
from metrics import Metrics

# System wide constants
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
            # Double loop to check sequence in ascending order
            if process_list[process].getArrivalTime() > process_list[process+1].getArrivalTime():
                process_list[process], process_list[process+1] = process_list[process+1], process_list[process]
                swapped = True
        if not swapped:
            # Loop breaks early if no swap occurs (smaller value, already in correct sequence)
            break

#Generate 100 dummy data for simulation.
def dummyGenerator() -> list[Pcb] | None:
    process_list: list[Pcb] = []
    for i in range(100):
        new_process = Pcb(i+1)
        process_list.append(new_process)
    sortProcessByArrivalTime(process_list) # Sorts the processes by arrival time to ease simulation
    return process_list

def roundRobin(time_quantum):
    # Universal clock timer
    time = 0
    # Initialize simulation required components
    process_list = dummyGenerator() # Available job list
    metrics = Metrics() # Statistics calculator
    cpu = CPU(time_quantum) # CPU 
    scheduler = Scheduler(process_list) # Scheduler
    # While there are still remaining cpu cycles
    while not (scheduler.ready_queue.isEmpty() and len(scheduler.getAvailableProcessList()) == 0 and cpu.checkIsIdle()):
        # Scheduler checks arrival of processes
        available_process = scheduler.filterAvailableProcess(time)
        if available_process and cpu.checkIsIdle():
            # CPU fetches process from scheduler and executes
            cpu.fetchNextProcess(scheduler)
            processing_time = cpu.executeProcess()
            # CPU finishes process, time leaping 
            time = time + processing_time
            # Scheduler checks for new arrival of processes during the time leap
            available_process = scheduler.filterAvailableProcess(time)
            # Scheduler decides where to place the executed process
            executed_process = scheduler.checkExecutedProcess(cpu.getCurrentProcess(), time)
            # Context switch penalty applies for completed/preempted process (guaranteed since CPU already handles it)
            time = time + CONTEXT_SWITCH 
            metrics.countContextSwitch() # Counting number of context switches
            if executed_process:
                # Process is added to completed queue 
                metrics.addCompletedProcess(executed_process)
            
        else:
            # No available jobs, advance time.
            time = time + 1

    # Display system statistics
    metrics.displaySystemMetrics()

def main():
    # Decide which simulation to run
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
