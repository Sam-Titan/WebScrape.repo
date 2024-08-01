# I have used the following libraries for the Web Scraping purposes
import requests
from bs4 import BeautifulSoup
import pandas as pd
# Here I use a header to access the website data
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Connection': 'keep-alive'
}
# Now i use request and BeautifulSoup function
url = "https://www.imdb.com/chart/top/"
response = requests.get(url, headers= headers)
soup = BeautifulSoup(response.content, 'html.parser')
data = soup.find('ul', attrs={'class' : 'ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 dHaCOW compact-list-view ipc-metadata-list--base'})
movies_name = []
movie_rating = []
movie_year = []
# Now i find the data i need by going to the website to inspect the code and access it
for store in data.find_all('li', attrs={'class' :'ipc-metadata-list-summary-item sc-10233bc-0 TwzGn cli-parent'}):
    # I now find the names and append them in a list
    movie_name = store.find('h3', class_='ipc-title__text').text
    movies_name.append(movie_name)
    # i once again do the same and deploy the data in a list
    movie_rating_0 = store.find('span', class_='ipc-rating-star--rating').text
    movie_rating.append(movie_rating_0)
    # Now  i again do the same append them accordingly
    movies_details = store.find('span', class_='sc-b189961a-8 hCbzGp cli-title-metadata-item').text
    movie_year.append(movies_details)
# Now i put the data in dict and then into panda dataframe and then to a csv file
dict = {'Rank and Name': movies_name, 'Ratings': movie_rating, 'Year':movie_year}
dp = pd.DataFrame(dict)
print(dp)
dp.to_csv('IMDB.Files', index=False)