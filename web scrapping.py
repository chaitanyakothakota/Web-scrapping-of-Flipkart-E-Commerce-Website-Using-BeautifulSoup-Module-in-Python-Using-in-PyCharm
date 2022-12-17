import requests
from bs4 import BeautifulSoup
url=input("Enter Url:- \n")
r=requests.get(url)
soup=BeautifulSoup(r.content,'html.parser')
p=soup.find('title').text
p1=soup.find(class_='B_NuCI').text
p2=soup.find('body').text
print("\n")
print("Website Title:- \n",p)
print("Mobile Model:- \n",p1)
print("information Data in Website:- \n",p2)
