from bs4 import BeautifulSoup
import requests

url = "https://www.iplt20.com/teams/royal-challengers-bengaluru/squad-details/164"

response=requests.get(url)

print(response)    # 200ok if server accepts

#print(response.text)

html_doc = response.text

soup = BeautifulSoup(html_doc , "html.parser")

details_label = soup.select('.grid-items > span')
details = soup.select('.grid-items > p')

# Output [<span>IPL Debut</span>, <span>Specialization</span>, <span>Date of Birth</span>, <span>Matches</span>] [<p>2008</p>, <p>Batter</p>, <p>05 November 1988</p>, <p>254</p>]

print (details_label , details)


for i in range (len (details_label)):
    print(details_label[i].text , details[i].text)

#print (soup.find_all('div' , class_ =  "grid-container"))