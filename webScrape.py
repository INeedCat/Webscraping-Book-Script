import requests
from bs4 import BeautifulSoup

url = ['https://novel22.net/eldest/page-' + str(j + 1) + '-' + str(1051729 + j) + '.html' for j in range(214)]

""" for i in url:
    print(i) """

writetofile = open(r"EldestBook.html", "a")

for i in range(len(url)):
    r = requests.get(url[i])
    
    soup = BeautifulSoup(r.content, 'html5lib')

    soup = soup.findAll('p')

    for s in range(len(soup)-2):
        writetofile.write(str(soup[s]) + '\n')

"""     x = input("Next Page")  """
writetofile.close()
