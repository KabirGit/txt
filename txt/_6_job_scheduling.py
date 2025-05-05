def job_schedule(jobs): 
    jobs.sort(key=lambda x: x[1], reverse=True) 
#     The jobs are sorted in descending order of profit using the sort() method.
# key=lambda x: x[1]: Extracts the second element (profit) of each tuple for sorting.
# reverse=True: Ensures the sorting is in descending order.
    max_deadline = max(jobs, key=lambda x: x[2])[2] 
#     This finds the maximum deadline among all jobs.
# key=lambda x: x[2]: Extracts the third element (deadline) of each tuple.
# [2]: Gets the deadline value from the job with the maximum deadline.
    slot = [False] * max_deadline 
#     A slot array is created to track whether a time slot is occupied.
# The size of the array is equal to the maximum deadline.
# Initially, all slots are set to False (unoccupied).
    profit = 0 
    n = len(jobs) 
    for i in range(n): 
        deadline = jobs[i][2] - 1 
        while deadline >= 0 and slot[deadline]: 
            deadline = deadline - 1 
#             For each job, start checking from its deadline (converted to a 0-based index).
# If the slot at the deadline is already occupied (slot[deadline] == True), move to the previous slot (deadline -= 1).
# Continue until a free slot is found or all earlier slots are checked.

        if deadline >= 0: 
            slot[deadline] = True 
            profit += jobs[i][1] 
    return profit
# If a free slot is found (deadline >= 0):
# Mark the slot as occupied (slot[deadline] = True).
# Add the job's profit to the total profit (profit += jobs[i][1]).

# jobs = [(1, 50, 2), (2, 10, 1), (3, 20, 2), (4, 30, 1), (5, 40, 3)] 
# print(job_schedule(jobs))


n = int(input("Enter the number of jobs: "))
jobs = []
for i in range(n):
    job_id = int(input(f"Enter Job ID for job {i + 1}: "))
    profit = int(input(f"Enter Profit for job {i + 1}: "))
    deadline = int(input(f"Enter Deadline for job {i + 1}: "))
    jobs.append((job_id, profit, deadline))

# Call the function and print the maximum profit
print("Maximum Profit:", job_schedule(jobs))