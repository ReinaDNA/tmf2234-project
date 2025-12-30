from pcb import Pcb

def main():
    #Universal clock timer
    time = 0
    counter = 0
    job_list: list[Pcb] = []
    #Generate 100 dummy data for simulation.
    for i in range(100):
        job_list.append(Pcb(i+1))
    
    while True:
        
        arrived_jobs: list[Pcb] = []
        if job_list:
            for job in job_list:
                if job.getArrivalTime() <= time:
                    arrived_jobs.append(job)
            for job in arrived_jobs:
                job_list.remove(job)
                counter = counter + 1
                print(f"Job {job.getProgramNumber()} has arrived at {job.getArrivalTime()}")

        time = time + 1
        if counter == 100:
            print(f"A total of {counter} programs has arrived.")
            return
    


main()
