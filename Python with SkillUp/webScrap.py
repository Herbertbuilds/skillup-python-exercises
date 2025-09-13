from bs4 import BeautifulSoup
import requests

#create a test html document
html_doc ="""<html>
<body>
<h1>Web Scrape test</h1>
<b><!-- This is a comment --></b>
<p title="About Me" class = "test">Hey you suckers...</p>
<div class="Cities">
<h2>Windhoek</h2>
</div>
</body>
</html>"""

#parse the html document
soup = BeautifulSoup(html_doc, 'html.parser')

#view the parsed document
#print(soup)

#create a tag object
tag = soup.p
#print(tag)

header = soup.h1.string
#print(header)

#print(tag.string)


#search tree tutorial
HTMLfilePath = HTMLfilePath = 'C:\\Users\\Herbert\\Documents\\Vs Code\\WAD Projects\\Lab3 ProfilePage\\index.html'

with open(HTMLfilePath, "r", encoding="utf-8") as html_file:
    content = html_file.read()
    soup2 = BeautifulSoup(content, 'html.parser')
    #print(soup2)

tag_li = soup2.find("li")

#check the type of the tag
#print(type(tag_li))

#print(tag_li)

#search_name = soup2.find_all(text = "Herbert")
#print(search_name)

#class_search = soup2.find_all(class_ = "hover-button")
#print(class_search)


#create an employee html doc
employee_doc = """<html>
<body>
<h1>EmployeeList</h1>

<employee class = "Software Engineer">
<Name>John Doe</Name>
</employee>

<employee class = "Data Scientist">
<Name>Jane Smith</Name>
</employee>

<employee class = "Web Developer">
<Name>Mike Johnson</Name>
</employee>

</body>
</html>"""

soup3 = BeautifulSoup(employee_doc, 'html.parser')

tag = soup3.employee
#print(tag)

#tag['class'] = "Full Stack Developer"
#print(tag)

#adding a new tag
add_tag = soup3.new_tag('age')
tag.string = '30'
soup3.employee.insert_after(add_tag)
#print(soup3)

tag.clear()
#print(soup3)

#web scraping time

url = 'https://genius.com/'
result = requests.get(url)
page_content = result.content
soup4 = BeautifulSoup(page_content, 'html.parser')
#print(soup4.prettify())
 