# algorithms-cheatsheet

## Python tricks

```python
a = ['?'] * N # initialize array
assert float('-inf') < -1000 < 1000 < float('+inf')
for i, elem in enumerate(["a", "b", "c"]):
	pass

assert [1, 2, 3][::-1] == [3, 2, 1]
assert [1, 2, 3][::2] == [1, 3]

"%r" % (True) # %r formats via repr

```

## Python Data Structures

### sets

```python
s = set()
s.add(3)
s.add(4)
s.remove(3)
```

### defaultdict

```python
from collections import defaultdict
d = defaultdict(int) # pass a constructor like int, list, tuple
d['a'] += 1
assert d['a']
```

### OrderedDict

### Counter

```python
from collections import Counter
C = Counter("abcefafgba")
assert C['a'] == 3
```

### heap

```python
pass
```

### queue

```python
pass
```

### rounding

```python
pass
```

### random numbers

### numerical base

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
