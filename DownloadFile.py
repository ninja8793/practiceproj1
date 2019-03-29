import urllib.request
import random

def download_web_image(url):
    name = random.randrange(1,1000)
    file_name=str(name)+".jpg"
    urllib.request.urlretrieve(url,file_name)


download_web_image("https://homepages.cae.wisc.edu/~ece533/images/fruits.png")
