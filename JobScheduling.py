def printJobScheduling(arr, t):
	n = len(arr)

	# Sort all jobs according to decreasing order of profit
	for i in range(n):
		for j in range(n - 1 - i):
			if arr[j][2] < arr[j + 1][2]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

	# To keep track of free time slots
	result = [False] * t

	# To store result (Sequence of jobs)
	job = ['-1'] * t

	# Iterate through all given jobs
	for i in range(len(arr)):
		# Find a free slot for this job 
        # (Note that we start from the last possible slot)
		for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
			# Free slot found
			if result[j] is False:
				result[j] = True
				job[j] = arr[i][0]
				break

	# print the sequence
	print(job)



# Practice
def job_scheduling(jobs, timeSlots):

	# Sort all the jobs according to the profit
	jobs.sort(key=lambda x: x[2], reverse=True)

	# To keep track of free time slots
	freeSlots = [False]*timeSlots

	# Store the answer - job names
	answer = [None]*timeSlots

	# Iterating over the jobs
	for i in range(len(jobs)):
		for j in range(min(timeSlots-1, jobs[i][1]-1)         ,-1,-1 ):		# Start, End, Reverse
			if freeSlots[j] is False:
				freeSlots[j] = True
				answer[j] = jobs[i][0]
				break
	print(answer)
		


# Driver's Code
if __name__ == '__main__':
	arr = [['a', 2, 100], # Job Array
			['b', 1, 19],
			['c', 2, 27],
			['d', 1, 25],
			['e', 3, 15]]

	print("Following is maximum profit sequence of jobs")
	printJobScheduling(arr, 3)
	job_scheduling(arr, 3)