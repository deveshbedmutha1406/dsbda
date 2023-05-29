import requests
from bs4 import BeautifulSoup as bs

with open('aws_review.html', 'r') as f:
    content = f.read()



soup = bs(content, 'html.parser')

print(soup.prettify())
names = soup.find_all('span', class_='a-profile-name')
print(names)

# extracting names
cust_names = [names[i].get_text() for i in range(len(names))]
print(cust_names)

#extracting review titles
titles = soup.find_all('a', class_='review-title-content')
title_list = [titles[i].select_one('span').get_text() for i in range(len(titles))]
print(title_list)
# extracting rating
ratings = soup.find_all('span',class_='a-icon-alt')
rating = [ratings[i].get_text() for i in range(len(ratings))]
print(rating)

import pandas as pd
from itertools import zip_longest

data = zip_longest(cust_names, title_list, rating, fillvalue=None)
df = pd.DataFrame(data)
df.to_csv('name2.csv')


