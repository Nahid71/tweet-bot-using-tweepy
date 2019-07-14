# model scraping for themodelbot

import requests
from bs4 import BeautifulSoup as bs
import os

# website with model images
url = 'https://www.pexels.com/search/python%20programming%20language/'

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll("img", {"class": "photo-item__img"})

# create directory for model images
if not os.path.exists('python-image'):
    os.makedirs('python-image')

# move to new directory
os.chdir('python-image')

# image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        # url = 'https://www.pexels.com/' + image['href']
        # new_url = url[:url.rfind(".")]
        url = image['src']
        # url = url[:url.rfind("?")]

        print(url)
        response = requests.get(url)

        if response.status_code == 200:
            with open('python-image-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass
