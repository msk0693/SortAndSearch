count = 0
def binary(n, key):
	global count 
	first = 0
	last = len(n)  -1
	while first <= last:
		count += 1
		mid = (first + last) // 2
		if key == n[mid] :
			return mid
		elif key < n[mid]:
			last = mid -1
		else :
			first = mid + 1
	return -1
def recursiveBinary(n, key):
	global count 
	count += 1
	if len(n) == 0:
		return -1
	else:
		mid = len(n) // 2
		if key == n[mid]:
			return mid
		elif key < n[mid]:
			return recursiveBinary(n[:mid], key)
		else:
			shift = mid + 1
			index = recursiveBinary(n[mid+1:], key)
			if index > -1:
				index += shift
			return index

def getCount():
	return count 
		
	