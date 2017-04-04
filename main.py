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
    index = {}
    graph = {}
    while to_crawl:
        # Update eventually with first link searched instead of last link searched
        page = to_crawl.pop()
        if(page not in crawled):
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(to_crawl, outlinks)
            crawled.append(page)
    return index, graph

def add_to_index(index,keyword,url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]
        
def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    return None


def add_page_to_index(index, url, content):
    # Improve keyword finding ability
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
        
def compute_ranks(graph):
    d = 0.8 # damping factor
    num_loops = 10 # arbitrary, but decent
    ranks = {}

    npages = len(graph) # nodes in the graph
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0, num_loops):
        new_ranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            newrank += sum([d *ranks[node] / len(graph[node]) for node in graph if page in graph[node]])
            new_ranks[page] = newrank
        ranks = new_ranks
    return ranks

index, graph = crawl_web("https://www.udacity.com/cs101x/urank/index.html")
ranks = compute_ranks(graph)
print index
print "/n"
print ranks

