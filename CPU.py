from pcb import Pcb
from scheduler import Scheduler
class CPU:
    BUSY = "Busy"
    IDLE = "Idle"

    def __init__(self, quantum):
        self.time_quantum = quantum
        self.current_process : Pcb = None
        self.state = CPU.IDLE

    def getCurrentProcess(self) -> Pcb | None:
        return self.current_process

    def fetchNextProcess(self, scheduler:Scheduler):
        self.current_process = scheduler.fetchNextProcess()
    
    def checkIsIdle(self):
        if self.state == CPU.IDLE:
            return True
        else:
            return False
        
    def executeProcess(self):
        if self.current_process is not None:
            process_burst_time = self.current_process.getBurstTime()
            self.state = CPU.BUSY
            execution_time = min(process_burst_time, self.time_quantum)
            remaining_burst_time = process_burst_time - execution_time
            if remaining_burst_time > 0:
                self.current_process.setBurstTime(remaining_burst_time)
                self.current_process.changeState(Pcb.READY)
                self.state = CPU.IDLE
                # print(f"burst remaining for {self.current_process.getProgramNumber()}: {self.current_process.getBurstTime()}")
                # print("Process Executed")
                return execution_time
            elif remaining_burst_time == 0:
                self.current_process.markAsComplete()
                self.state = CPU.IDLE
                print("Process Completed.")
                return execution_time
            else:
                print("An error occured. Exiting Execution Process.")
                
        else:
            print("Error, CPU does not hold a process.")
            
