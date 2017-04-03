# Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

# WEB CRAWLER 
# LESSON 3

def get_page(url):
    # This is a simulated get_page procedure so that you can test your
    # code on two pages "http://xkcd.com/353" and "http://xkcd.com/554".
    # A procedure which actually grabs a page from the web will be 
    # introduced in unit 4.
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""
    return ""

# Union method from previous quiz
def union(l1, l2):
    for e in l2:
        if(e not in l1):
            l1.append(e)

# start_link contains the value of the first position on the page that contains a link
def get_next_target(S):
    start_link = S.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = S.find('"',start_link)
    end_quote = S.find('"',start_quote + 1)
    url = S[start_quote+1:end_quote]
    return url, end_quote

def get_all_links(S):
    links = []
    while True:
        url, endpos = get_next_target(S)
        if url:
            links.append(url)
            S = S[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    to_crawl = [seed]
    crawled = []
    index=[]
    while to_crawl:
        # Update eventually with first link searched instead of last link searched
        page = to_crawl.pop()
        if(page not in crawled):
            content = get_page("http://xkcd.com/353")
            add_page_to_index(index, page, content)
            union(to_crawl, get_all_links(content))
            crawled.append(page)
    return index

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return index
    index.append([keyword,[url]])
    return index

def lookup(index,keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []


def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
        
print crawl_web([])

