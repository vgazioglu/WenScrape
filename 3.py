import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml

URL = 'https://www.tff.org/Default.aspx?pageId=30&kisiId=1330123'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_PageView3')


#print(results.prettify())

#job_elems = results.find_all('table', class_='GridAltRow_TFF_Contents')

#for job_elem in job_elems:
 #   print(job_elem, end='\n'*2)
#    continue

My_table = soup.find('table',{'class':'MasterTable_TFF_Contents'})

#print(My_table)


#tables = pd.read_html(My_table)
#print(tables)

"""inks = My_table.findAll('td')
print(links)

Countries = []
for link in links:
    Countries.append(link.get('ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_grdTakimlar_ctl01_ctl06_ot'))

#print(Countries)

for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('a', id='ctl00_MPane_m_30_202_ctnr_m_30_202_OyuncuIstatistikDisplay1_grdTakimlar_ctl01_ctl04_ot')
   # company_elem = job_elem.find('div', class_='company')
   # location_elem = job_elem.find('div', class_='location')
    print(title_elem)
    #print(company_elem)
    #print(location_elem)
    print()

for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()

python_jobs = results.find_all('h2', string='Python Developer')

python_jobs = results.find_all('h2',
                               string=lambda text: "python" in text.lower())

for p_job in python_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")"""