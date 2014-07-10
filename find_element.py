liste=[4,3,8,1,9]
nb=1
def find_list(liste,nb):
	if nb in liste:
		v=liste.index(nb)
		return v
	else:
		print("-1")
print(find_list(liste,9))
