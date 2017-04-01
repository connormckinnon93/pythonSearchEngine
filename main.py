# Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

# Page contents provided by udacity instructor
page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="/">'''

# start_link contains the value of the first position on the page that contains a link
start_link = page.find('<a href=')
start_quote = page.find('"',start_link)
end_quote = page.find('"',start_quote + 1)
url = page[start_quote+1:end_quote]


# Print results of start_link
print url