import requests
import bs4

courses_names = []
response = requests.get("https://rahulshettyacademy.com/AutomationPractice/")
soup = bs4.BeautifulSoup(response.content,'html.parser')
courses = soup.find('table',{'name':'courses'})

rows = courses.findAll('tr')

for each_row in range(1,len(rows)):
    # for each_row in rows[1:]:
    rowdata = rows[each_row].findAll('td')
    courses_names.append(rowdata[1].text)

print(courses_names)