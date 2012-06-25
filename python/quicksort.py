def quicksort(L):
	if L == []:
		return L
	pivot = L[0]
	lesser = quicksort([x for x in L[1:] if x <= pivot])
	greater = quicksort([x for x in L[1:] if x > pivot])
	return lesser + [pivot] + greater

print(quicksort([3, -1, 2, 0, 7, 100]))
