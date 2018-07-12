def sort_by_height_difference(queue):
	for i in range(len(queue)):
		for j in range(len(queue)):
			if queue[i][1]>queue[j][1]:
				queue[i],queue[j] = queue[j],queue[i]
			elif queue[i][1] == queue[j][1] and queue[i][0]>queue[j][0]:
				queue[i],queue[j] = queue[j],queue[i]


	return queue[::-1]

def sort_by_height(queue):
	i=0
	for i in range(len(queue)):
		



test_cases= [[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]],
			[[12,0],[6,3],[3,4],[9,2],[11,1],[1,5]],
			[[2,4], [5,1], [3,3], [1,5], [4,2], [6,0]]]

outputs = [[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]],
			[[12,0],[11,1],[9,2],[6,3],[3,4],[1,5]],
			[[6,0], [5,1], [4,2], [3,3], [2,4], [1,5]]
		  ]
j=0

# print(test_cases)
for test_case in test_cases:
	# print(test_case)
	print(sort_by_height_difference(test_case))
	a=(outputs[j]==sort_by_height_difference(test_case))
	if not a:
		b=(outputs[j] == sort_by_height(test_case))
	j+=1



"""
def sort_by_height_difference(queue):
	for i in range(len(queue)):
		for j in range(len(queue)):
			if queue[i][1]>queue[j][1]:
				if queue[i][0]<queue[j][0]:
					queue[i],queue[j] = queue[i],queue[j]
				else:
					queue[i],queue[j] = queue[j],queue[i]
			elif queue[i][1] == queue[j][1] and queue[i][0]>queue[j][0]:
				queue[i],queue[j] = queue[j],queue[i]

	return queue[::-1]
"""

