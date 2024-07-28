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
movie_all = []
movie_year = []
movie_rank = []
movie_runtime = []
movie_appropriate = []
# for ranking the movies
for el in range(1,26):
    movie_rank.append(el)
# Now i find the data i need by going to the website to inspect the code and access it
for store in data.find_all('li', attrs={'class' :'ipc-metadata-list-summary-item sc-10233bc-0 TwzGn cli-parent'}):
    movie_name = store('h3', class_='ipc-title__text')
    # I was unable to deploy the text or get_text function even after using the find function before 
    # After getting the names to remove the unnecessary text i use splicing. 
    movie_name_1 = str(movie_name)
    movie_name_splice = movie_name_1[32:]
    movie_name_splice = movie_name_splice[:-6]
    # movie_movie_splice is the variable for spliced element
    movies_name.append(movie_name_splice)
    # i once again do the same and deploy the data in a list
    movie_rating_0 = store('span', class_='ipc-rating-star--rating')
    movie_rating_1= str(movie_rating_0)
    movie_rating_splice = movie_rating_1[39:]
    # movie_rating_splice is the variable for spliced element
    movie_rating_splice = movie_rating_splice[:-8]
    movie_rating.append(movie_rating_splice)
    # Now to filter the runtime and Rated Text i deploy a loop to splice and get readable text
    for row in store('span', class_='sc-b189961a-8 hCbzGp cli-title-metadata-item'):
        row_1 = str(row)
        # row_splice is the spliced element
        row_splice = row_1[59:]
        row_splice = row_splice.replace("</span>",'')
        movie_all.append(row_splice)
        
# Now i deploy a loop to get year of release, runtime and Rated out of the list
a = 0
b = 1
c = 2
while a < 75:
    movie_year.append(movie_all[a])
    a += 3
    movie_runtime.append(movie_all[b])
    b += 3
    movie_appropriate.append(movie_all[c])
    c += 3

# Now i put the data in dict and then into panda dataframe and then to a csv file
dict = {'Rank': movie_rank, 'Name': movies_name, 'Ratings': movie_rating, 'Year':movie_year, 'Runtime':movie_runtime, 'Rated':movie_appropriate}
dp = pd.DataFrame(dict)
print(dp)
dp.to_csv('IMDB.Files',index=False)
