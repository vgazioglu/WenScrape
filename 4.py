import requests
from bs4 import BeautifulSoup
import pandas as pd


def futbolcu_hareket_bilgileri(futbolcu_URL):
    URL = futbolcu_URL
    # URL = 'https://www.tff.org/Default.aspx?pageId=30&kisiId=1055923'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())
    my_table2 = soup.find('table', {'class': 'yuzdeyuzH'})
    # print(my_table2)

    my_table = soup.find('table', {'class': 'MasterTable_TFF_Contents'})
    # print(My_table)

    # table = soup.find('table', border=1)
    rows_output = my_table.find_all('tr')
    # print(type(rows))
    # print(rows)
    rn_list = []
    sr_list = []
    dn_list = []
    nn_list = []
    for row in rows_output:
        data = row.find_all("td")
        if len(data) > 0:
            # rn =
            rn_list.append(data[0].get_text().strip())
            sr_list.append(data[1].get_text().strip())
            dn_list.append(data[2].get_text().strip())
            nn_list.append(data[3].get_text().strip())
            sr = data[1].get_text()
            d = data[2].get_text()
            n = data[3].get_text()
            # print(str(rn).strip() + "\t" + sr + "\t" + d + "\t" + n)
            # print(rn_list)

    weather = pd.DataFrame({
        "KULÜP": rn_list,
        "İLK VİZE": sr_list,
        "SON VİZE": dn_list,
        "DURUM": nn_list
    })
    print(weather)
    weather.to_csv("futbolcu_bilgileri.csv")


"""for i in range(105933, 105944):
    futbolcu_hareket_bilgileri('https://www.tff.org/Default.aspx?pageId=30&kisiId='+str(i)+'')"""

futbolcu_hareket_bilgileri('https://www.tff.org/Default.aspx?pageId=30&kisiId=1055923')
