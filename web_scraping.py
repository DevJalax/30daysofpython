from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("C:/Users/JALAX/Desktop/chromedriver.exe")
company = [] 
position = []
driver.get("https://internshala.com/internships/matching-preferences")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.find_all('a',href=True,attrs={'class':'individual_internship_header'}):
    position = a.find('div',attrs={'class':'heading_4_5 profile'})
    company = a.find('div',attrs={'class':'heading_6 company_name'})
    position.append(position.text)
    company.append(company.text)

df = pd.DataFrame({'Position':position,'company':company}) 
df.to_csv('internshala.csv', index=False, encoding='utf-8')