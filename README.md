# interview-cheatsheet

## Python

### Sets

```python
s = set()
s.add(3)
s.add(4)
s.remove(3)
```

### OrderedDict

### Counter

### heap

## Algorithms

### Binary Search

```python
def binary_search(arr, target):
	i, j = 0, len(arr) # search on [i, j)
	while j - i > 1:
		mid = (i + j) // 2

		if arr[mid] == target: return mid
		elif arr[mid] < target: i = mid
		else: j = mid

	if arr[i] == target: return i
	return None
```
