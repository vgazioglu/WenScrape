import requests
from bs4 import BeautifulSoup
import sys


def futbolcu_hareket_bilgileri(futbolcu_URL):
    URL = futbolcu_URL
    # URL = 'https://www.tff.org/Default.aspx?pageId=30&kisiId=1055923'
    page = requests.get(URL)



    soup = BeautifulSoup(page.content, 'html.parser')

    #print(soup.prettify())
    #sys.exit(0)

    My_table2 = soup.find('table', {'class': 'yuzdeyuzH'})
    print(My_table2)
    sys.exit(0)

    My_table = soup.find('table', {'class': 'MasterTable_TFF_Contents'})
    # print(My_table)

    # table = soup.find('table', border=1)
    rows = My_table.find_all('tr')

    for row in rows:
        data = row.find_all("td")
        if len(data) > 0:
            rn = data[0].get_text()
            sr = data[1].get_text()
            d = data[2].get_text()
            n = data[3].get_text()
            print(str(rn).strip() + "\t" + sr + "\t" + d + "\t" + n)

"""for i in range(105933, 105944):
    futbolcu_hareket_bilgileri('https://www.tff.org/Default.aspx?pageId=30&kisiId='+str(i)+'')"""


futbolcu_hareket_bilgileri('https://www.tff.org/Default.aspx?pageId=30&kisiId=1055923')