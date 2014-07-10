links=open("link_box","a")
liste=[]
liste2=liste.append(links)
begin=("http://www.google.")
google=("google")
def onl(google):
	for e in liste2:
		if begin in e:
			print(e)
		return e
print(onl(google))
links.close()