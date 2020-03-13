from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


#from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.common.keys import Keys
#driverLocation = '/usr/bin/chromedriver' #if windows
#driver = webdriver.Chrome(driverLocation)
#driver.get('http://arithmetic.zetamac.com/game?key=a7220a92')
#element = driver.find_element_by_link_text('problem')
#print(element)


options = webdriver.ChromeOptions()
options.add_argument('user-agent = Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/bin/chromedriver')
#driver.get('https://www.google.co.in')


#driver = webdriver.Chrome("/usr/bin/chromedriver")
#driver = webdriver.Chrome(executable_path='chromedriver')


products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')