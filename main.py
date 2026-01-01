from pcb import Pcb
from CPU import CPU
from queues import CompletedQueue
from scheduler import Scheduler
TIME_QUANTUM = 3
#Generate 100 dummy data for simulation.
def dummyGenerator() -> list[Pcb] | None:
    job_list: list[Pcb] = []
    for i in range(5):
        job_list.append(Pcb(i+1))
    return job_list

def main():
    #Universal clock timer
    time = 0
    job_list = dummyGenerator()
    completed = CompletedQueue()
    cpu = CPU(TIME_QUANTUM)
    scheduler = Scheduler(job_list)
    # print(scheduler.ready_queue.isEmpty(),len(scheduler.getAvailableProcessList()),cpu.checkIsIdle())
    while not (scheduler.ready_queue.isEmpty() and len(scheduler.getAvailableProcessList()) == 0):
        # print(scheduler.ready_queue.isEmpty(),len(scheduler.getAvailableProcessList()),cpu.checkIsIdle())
    # while count < 30:
        available_job = scheduler.filterAvailableProcess(time)
        if available_job and cpu.checkIsIdle():
            cpu.fetchNextProcess(scheduler)
            processing_time = cpu.executeProcess()
            time = time + processing_time
            executed_process = scheduler.checkExecutedProcess(cpu.getCurrentProcess())
            if executed_process:
                completed.addProcess(executed_process)
            else:
                print(f"Execution for {cpu.current_process.getProgramNumber()} completed, next loop...")
        else:
            print("Don't have jobs available, forwarding time...")
            time = time + 1

        print(f"The time now is {time}ms")
        for process in scheduler.ready_queue.getQueueList():
            print(process.getProgramNumber())
        if time > 150:
            break

main()
