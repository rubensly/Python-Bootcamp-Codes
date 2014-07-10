a=[1,2,3]
b=[4,5,6]
def union(a,b):
	for e in b:
		a.append(e)
	return a
print(union(a,b))