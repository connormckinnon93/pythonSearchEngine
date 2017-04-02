# Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

# WEB CRAWLER 
# LESSON 2

# Page contents provided by udacity instructor
page = '''<div id="top_bin"> <div id="top_content" class="width960"><div class="udacity float-left"> <a href="/">'''

# start_link contains the value of the first position on the page that contains a link
def get_next_target(S):
    start_link = S.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = S.find('"',start_link)
    end_quote = S.find('"',start_quote + 1)
    url = S[start_quote+1:end_quote]
    return url, end_quote

def print_all_links(S):
    while True:
        url, endpos = get_next_target(S)
        if url:
            print url
            S = S[endpos:]
        else:
            break

# Print results of start_link
# get_page defined in Lesson 4
print print_all_links(get_page('http://xkcd.com/353'))

