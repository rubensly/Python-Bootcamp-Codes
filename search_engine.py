page=("<a href='http://www.google.com'/>hghh<a href='http://www.bing.com'/>ngfdirjsfnjjfjk<a href='http://www.google.fr'>jdfnl vsib<a href='http://www.google.ht'>")
def get_next_link(page):
	start_link=page.find("href")
	start_quote=page.find("'",start_link)+1
	end_quote=page.find("'",start_quote)
	url=page[start_quote:end_quote]
	return url,end_quote

def print_all_links(page):
	links=[]
	while 1:
		url,end_quote=get_next_link(page)
		if url != "":
			if "http://" in url:
				links.append(url)
				page=page[end_quote:]
			else:
				page=page[end_quote:]
		else:
			break
	return links


input=input("saisissez votre lien:")
links=print_all_links(page)
def searching(input,links):
	for e in links:
		if input in e:
			print(e)
print(searching(input,links))
		

links=print_all_links(page)
box=open("link_box","a")
for e in links:
	a=box.write(e+"\n")
box.close()

			