import requests
import json
from bs4 import BeautifulSoup
import shutil

for x in range(15,30):
    urls = []
    containerPage = 'https://www.oldbookillustrations.com/illustrations/page/' + str(x) + '/'
    page = requests.get(containerPage)
    soup = BeautifulSoup(page.content, 'html.parser')

    figures = soup.find(class_="archive-gallery").find_all('figure')
    singlePagelinks = []
    for figure in figures:
        singlePagelinks.append(figure.find("a", href=True)['href'])

    jsonLinks = []
    for link in singlePagelinks:
        jsonLinks.append('https://www.oldbookillustrations.com/wp-content/files/json-records/' + link.split('/')[-2] + '.json')

    imageLinks = []
    for link in jsonLinks:
        response = requests.get(link)
        if response.status_code == requests.codes.ok:
            try:
                imageLinks.append(json.loads(response.text)['illustration'][-1]['image_url'])
                print(link)
            except:
                print('Error parsing ' + link)
                continue

    for link in imageLinks:
        response = requests.get(link, stream=True)
        with open('scraped_images/' + link.split('/')[-1], 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response