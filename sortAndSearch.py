import random
import mergeSort
import search

#SEARCH DISPLAY
def display(key, index, count):
	if index == -1 :
		print "\n%i not in List\nSearch Iterations: %i\n" % (key, count)
	else :
		print "\n%i found at index %i\nSearch Iterations: %i\n"  % (key, index, count)


n = int(input("Enter size to generate a list of random integers "))
while n <= 1 :
	n = int(input("Please enter a size higher then one "))

l = []
print "Unsorted list:"
for i in xrange(n):
	rn = random.randint(0,100)
	l.append(rn)
	print l[i]

#SORT
recursive = raw_input("Would you like to merge recursively?(y/n) ")
sorted = mergeSort.mergeSort(l, recursive)
print "\nSorted list:"
for i in sorted:
	print i 
count = mergeSort.getCount()
print "Sort Iterations: %i\n" % (count)
 
#SEARCH
searchOption = raw_input("Would you like to search for an item in the list?(y/n) ")
if searchOption.lower() == 'y':
	recursive = raw_input("Would you like to search recursively?(y/n) ")
	key = int(input("Enter key to search in List "))
	if recursive.lower() == 'y':
		index = search.recursiveBinary(sorted, key)
	else :
		index = search.binary(sorted, key)
	searchCount = search.getCount()
	display(key, index, searchCount)
	count += searchCount

print "Total Iterations: %i" % (count) 
	
