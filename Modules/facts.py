# from bs4 import BeautifulSoup as BS
# import requests
# import random
#
# # def get_facts():
# req="https://www.lingoda.com/en/blog/fun-facts-english-language"
# res=requests.get(req)
# soup = BS(res.text, 'html.parser')
# list=[x.text for x in soup.find_all('ol')]
#     # return random.choice(list)
#
# p=random.choice(list)
# print(p)
import requests
from bs4 import BeautifulSoup as BS
import random

def get_facts():
    req = 'https://www.bloomsbury-international.com/blog/2014/07/11/15-interesting-facts-about-the-english-language/'
    res = requests.get(req)
    soup = BS(res.text, 'html.parser')
    list = [x.text for x in soup.find_all('p')]
    list=list[3:18]
    # for item in list:
    #     print(item+"\n")
    fact=random.choice(list)
    fact=fact.split(' ',1)
    return fact[1]
# print(get_quotes())
