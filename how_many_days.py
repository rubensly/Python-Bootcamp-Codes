year=[31,28,31,30]
janvier=1
fevrier=2
def how_many_days(janvier):
	pos=janvier
	function=year[pos-1:pos]
	return function
print(how_many_days(fevrier))