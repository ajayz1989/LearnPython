
# for fetching the data from a URL and then printing it
from urllib.request import urlopen

response = urlopen('http://sixty-north.com/c/t.txt')
data = []
for line in response:
    line_words = line.decode().split()
    for word in line_words:
        data.append(word)
        print('----------')
for word in data:
    print(word)

# for printing the text inside the banner
def bannerText(text,border):
    border = border * len(text)
    print(border)
    print(text)
    print(border)


bannerText("Ajay Kumar", "-")

#time functions
import time
print(time.ctime())



