#!/usr/bin/env python
import random

def kth(L, k):
	le = []
	eq = []
	gt = []
	pivot = L[random.randint(0, len(L))]
	for e in L:
		if e < pivot:
			le.append(e)
		elif e > pivot:
			gt.append(e)
		else:
			eq.append(e)
	if k <= len(gt):
		return kth(gt, k)
	elif k <= (len(gt) + len(eq)):
		return pivot
	else:
		return kth(le, (k - len(gt) - len(eq)))

print(kth(range(1000), 5))
