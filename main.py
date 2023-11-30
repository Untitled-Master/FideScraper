import requests
from bs4 import BeautifulSoup

#profile
url = 'https://ratings.fide.com/profile/1503014'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#info
data_tags = soup.findAll('div', class_='profile-top-info__block__row__header')
data = soup.findAll('div', class_='profile-top-info__block__row__data')

for data_tag, info in zip(data_tags, data):
  print(f"{data_tag.text} {info.text}")


#rating
rating_std = soup.find('div', class_='profile-top-rating-data profile-top-rating-data_gray')
rating_text = rating_std.text.strip().replace('\n', '').replace('  ', '').replace('std', 'Classical: ')
print(rating_text)

