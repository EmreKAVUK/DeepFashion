import requests
from bs4 import BeautifulSoup
category_name = ["t-shirt","pantolon","boxer","kazak","ayakkabi","dis-giyim","sweatshirt","gomlek","elbise","bluz","etek","sort"]
categories_url = ["https://www.boyner.com.tr/erkek-t-shirt-modelleri-c-200107/","https://www.boyner.com.tr/erkek-pantolon-modelleri-c-200105/","https://www.boyner.com.tr/erkek-boxer-c-3392727/","https://www.boyner.com.tr/erkek-kazak-hirka-modelleri-c-200101/1/?filterIDList=20967/","https://www.boyner.com.tr/erkek-ayakkabi-p-c-2004/","https://www.boyner.com.tr/erkek-dis-giyim-c-3392750/","https://www.boyner.com.tr/erkek-sweatshirt-c-200106/1/?filterIDList=20715/","https://www.boyner.com.tr/erkek-gomlek-modelleri-c-200104/","https://www.boyner.com.tr/kadin-elbise-modelleri-c-100101/","https://www.boyner.com.tr/kadin-gomlek-bluz-c-100102/","https://www.boyner.com.tr/kadin-etek-modelleri-c-100108/","https://www.boyner.com.tr/erkek-sort-c-3302071/"]

def pull_data(url,cname):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.findAll('img', class_='lazy')
    for image in images:
        name = image['alt']
        link = image['data-original']

        try:
            with open("C:\\Users\\pc\\Desktop\\DeepLearning_Project\\input\\clothes\\images\\"+cname+"\\"+name.replace(' ','-').replace('/','').lstrip()+'.jpg','wb') as f:
                im = requests.get(link)
                f.write(im.content)
        except:
            pass
page=1
index = 0
for category in categories_url:
    while page < 24:
        url = category+str(page)+"/?orderOption=Editor"
        page+=1
        ctgry = category_name[index]
        pull_data(url,ctgry)
        print()
    page=1
    index+=1
page=1
index = 0