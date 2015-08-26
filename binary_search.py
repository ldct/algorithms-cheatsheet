#!/usr/bin/env python3
def binary_search(arr, target):
	# find i such that arr[i] == target
	i, j = 0, len(arr) # search on [i, j)

	while j - i > 1:
		mid = (i + j) // 2

		if arr[mid] == target:
			return mid
		elif arr[mid] < target:
			i = mid
		else:
			j = mid

	if arr[i] == target:
		return i

	return None

print(binary_search([-2, 5, 7], 5))

def binary_search_ub(arr, upper_bound):
	# find minimal i such that arr[i] <= upper_bound
	pass