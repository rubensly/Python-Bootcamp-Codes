school=("Columbia University")
student=(400)
fees=(45000)
def total_enroll(school,student,fees):
	total=student*fees
	a=("le nbre d'eleves est")
	b=("le total est")
	c=a,student
	d=b,total
	return c,d
print(total_enroll(school,student,fees))