page=("<a href='google.com'/>hghh<a href='bing.com'/>")
def get_next_link(page):
	start_link=page.find("a href=")
	start_quote=page.find("'",start_link)
	end_quote=page.find("'",start_quote+1)
	url=page[start_quote:end_quote]
	return(url,end_quote)

def print_all_links(page):
	links=[]
	while True:
		url,end_quote=get_next_link(page)
		if url != "":
			if "http://www." in url:
				links.append(url)
				page=page[end_quote:]
			else:
				page=page[end_quote:]
		else:
			break
	return links
print(print_all_links(page))
			