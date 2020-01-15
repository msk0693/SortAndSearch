count = 0
def mergeSort(n, option):
	global count 
	count+= 1
	if len(n) <= 1:
		return n
	else:
		mid = len(n) // 2
		left = mergeSort(n[:mid], option)
		right = mergeSort(n[mid:], option)
		if option.lower() == 'y':
			return recursiveMerge(left, right)
		else :
			return merge(left, right)
def merge(left, right):
	global count
	result = []
	l = 0
	r = 0
	while l < len(left) and r < len(right):
		count += 1
		if left[l] <= right[r]: #Stable Search
			result.append(left[l])
			l += 1
		else:
			result.append(right[r])
			r += 1
	if l == len(left):
		result += right[r:]
	else:
		result += left[l:]
	return result 
def recursiveMerge(left, right):
	global count
	count += 1
	if not right:
		return left
	if not left:
		return right
	if left[0] <= right[0] :
		return [left[0]] + recursiveMerge(left[1:], right)
	return [right[0]] + recursiveMerge(left, right[1:])
def getCount():
	return count


