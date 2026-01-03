from pcb import Pcb
from scheduler import Scheduler
class CPU:
    # Constant variables for CPU states
    BUSY = "Busy"
    IDLE = "Idle"

    #Constructor
    def __init__(self, quantum):
        self.time_quantum = quantum
        self.current_process : Pcb = None
        self.state = CPU.IDLE

    def executeProcess(self):
        #Main Method of the CPU
        if self.current_process is not None: #Checks if there is a process in the CPU
            #Change states 
            self.state = CPU.BUSY 
            self.current_process.changeState(Pcb.RUNNING)
            #Check burst time against time quantum
            process_burst_time = self.current_process.getBurstTime() 
            execution_time = min(process_burst_time, self.time_quantum)
            remaining_burst_time = process_burst_time - execution_time
            #Checks and decides what to do based on remaining burst time
            if remaining_burst_time > 0:
                #If program is preempted (has remaining burst time)
                self.current_process.setBurstTime(remaining_burst_time) #Set remaining burst time back to the PCB.
                self.current_process.changeState(Pcb.READY) # Set PCB state back to READY.
                self.state = CPU.IDLE # Idles the CPU.
                return execution_time # Returns the time so the main loop can advance time
            elif remaining_burst_time == 0:
                #If program is completed (no remaining burst time)
                self.current_process.markAsComplete() # Mark the program as completed.
                self.state = CPU.IDLE 
                return execution_time
            else:
                # Error handling 
                print("An error occured. Exiting Execution Process.")
        else:
            # Error handling (If there are no processes in CPU)
            print("Error, CPU does not hold a process.")
            
    # Getters
    def getCurrentProcess(self) -> Pcb | None:
        return self.current_process

    # Calls the scheduler to pass in the next process.
    def fetchNextProcess(self, scheduler:Scheduler):
        self.current_process = scheduler.fetchNextProcess()
    
    # Function for main loop to check if CPU is idle or not
    def checkIsIdle(self):
        if self.state == CPU.IDLE:
            return True
        else:
            return False