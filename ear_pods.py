from bs4 import BeautifulSoup

with open("amazon_review.html") as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')

# parent = soup.find(id="cm_cr-review_list")
# for ele in parent.children:
#     print(ele)

parent = soup.find_all(attrs={"data-hook": "review"}, class_="a-section review aok-relative")
print(len(parent))
# profile name
print(parent[0].find('span', class_='a-profile-name').get_text())

print(parent[0].find('span', class_='a-icon-alt').get_text())
print(parent[0].find('span', attrs={'data-hook':'review-date'}).get_text())
print(parent[0].find('span', attrs={'data-hook': 'review-body'}).contents[1].get_text())


profileName = []
rating = []
review_date = []
reviews = []

for ele in parent:
    profileName.append(ele.find('span', class_='a-profile-name').get_text())
    rating.append(ele.find('span', class_='a-icon-alt').get_text())
    review_date.append(ele.find('span', attrs={'data-hook':'review-date'}).get_text())
    reviews.append(ele.find('span', attrs={'data-hook': 'review-body'}).contents[1].get_text())

import pandas as pd
from itertools import zip_longest

data = zip_longest(profileName, rating, review_date, reviews, fillvalue=None)
df = pd.DataFrame(data, columns=['User', 'Rating', 'Date', 'Review'])
df.to_csv('aws.csv')