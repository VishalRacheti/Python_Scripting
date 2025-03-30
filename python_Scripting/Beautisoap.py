from bs4 import BeautifulSoup

html_doc = """

<html>
<head>
  <title>This is the title of the document</title>
</head>

<body>
  <h1>This is a heading</h1>
  <p>This is a paragraph.</p>
  <a href="https://www.google.com">Google</a>
</body>

</html>


"""



soup = BeautifulSoup (html_doc , 'html.parser')

print (soup.title.string) # Output This is the title of the document

print(soup.find('p').string) #Output This is a paragraph.

print(soup.find('p')) # Output <p>This is a paragraph.</p>

print(soup.find('a').get('href')) # Output https://www.google.com

print (soup.find("a")) # Output <a href="https://www.google.com">Google</a>