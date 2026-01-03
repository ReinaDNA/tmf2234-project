from pcb import Pcb

class Metrics:
    def __init__(self):
        self.completed_processes: list[Pcb] = []
        self.context_switch = 0

    def countContextSwitch(self):
        self.context_switch = self.context_switch + 1

    def getContextSwitchCount(self):
        return self.context_switch
    
    def getCPUOverhead(self):
        return self.context_switch*1.0

    def addCompletedProcess(self, newProcess):
        self.completed_processes.append(newProcess)

    def calculateMetrics(self):
        # print("\n=== Results for each Process ===\n")
        self.sortProcessByProgramNumber(self.completed_processes)
        for process in self.completed_processes:
            process.setTurnaroundTime()
            process.setWaitingTime()
            print(f"Program #{process.getProgramNumber()}\n")
            print(f"Finish time: {process.getFinishTime()}ms\n")
            print(f"Turnaround time: {process.getTurnaroundTime()}ms\n")
            print(f"Waiting time: {process.getWaitingTime()}ms\n")

    def displaySystemMetrics(self):
        self.calculateMetrics()
        print(f"Average Turnaround Time: {self.calculateAverageTurnaroundTime()}ms")
        print(f"Average Waiting Time: {self.calculateAverageWaitingTime()}ms")
        print(f"Total Number of Context Switches: {self.getContextSwitchCount()}")
        print(f"Total CPU Overhead caused By Context Switching: {self.getCPUOverhead()}ms")

    def calculateAverageWaitingTime(self):
        total = 0
        for process in self.completed_processes:
            total = total + process.getWaitingTime()
        return (total/len(self.completed_processes))
     
    def calculateAverageTurnaroundTime(self):
        total = 0
        for process in self.completed_processes:
            total = total + process.getTurnaroundTime()
        return (total/len(self.completed_processes))

    def sortProcessByProgramNumber(self, process_list:list[Pcb]):
        #Simple bubble sort function 
        #Sorting the processes by Program Number as each program reaches the completed queue in random order.
        n = len(process_list)
        for i in range(n):
            swapped = False
            for process in range(0, n-i-1):
                if process_list[process].getProgramNumber() > process_list[process+1].getProgramNumber():
                    process_list[process], process_list[process+1] = process_list[process+1], process_list[process]
                    swapped = True
            if not swapped:
                break