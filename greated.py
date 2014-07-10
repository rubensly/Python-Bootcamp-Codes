l=[4,57,8,4,282,74]
	
def greated(l):
	plus_grand=0
	for number in l:
		if plus_grand < number:
			plus_grand=number
		else:
			print()
	return(plus_grand)
print(greated(l))