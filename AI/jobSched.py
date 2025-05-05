# Job class
class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs):
    # Sort jobs by descending profit
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    max_deadline = max(job.deadline for job in jobs)
    slots = [None] * max_deadline  # Time slots

    total_profit = 0
    scheduled = []

    for job in jobs:
        for i in range(min(max_deadline, job.deadline) - 1, -1, -1):
            if slots[i] is None:
                slots[i] = job.id
                total_profit += job.profit
                scheduled.append(job.id)
                break

    return scheduled, total_profit

# Sample job list
jobs = [
    Job('A', 2, 100),
    Job('B', 1, 19),
    Job('C', 2, 27),
    Job('D', 1, 25),
    Job('E', 3, 15)
]

scheduled_jobs, profit = job_scheduling(jobs)
print("Scheduled Jobs:", scheduled_jobs)
print("Total Profit:", profit)
