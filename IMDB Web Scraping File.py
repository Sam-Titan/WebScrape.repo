# I have used the following libraries for the Web Scraping purposes
import requests
from bs4 import BeautifulSoup
import pandas as pd
# Here I use a header to access the website data
url = "https://www.imdb.com/chart/top/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Connection': 'keep-alive'
}
# Now i use request and BeautifulSoup function
def fectch_imdb_top_movie(url, headers):
    global soup
    # Now i find the data i need by going to the website to inspect the code and access it
    response = requests.get(url, headers=headers)
    if 200 == response.status_code:
        soup = BeautifulSoup(response.content, 'html.parser')
        print(response.status_code)
    else: 
        print("Cannot find the page for webscraping or not getting a response")
        soup = 'Error'
def parse_data(soup):
    global movie_name
    global movie_rating
    global movie_year
    movie_name = []
    movie_year = []
    movie_rating = []
    if soup != 'Error':
        for store in soup.find_all('li', attrs={'class' :'ipc-metadata-list-summary-item sc-10233bc-0 TwzGn cli-parent'}):
            # I now find the names and append them in a list
            movie_detail = store.find('h3', class_='ipc-title__text').text
            movie_name.append(movie_detail)

            # i once again do the same and deploy the data in a list
            movie_detail = store.find('span', class_='ipc-rating-star--rating').text
            movie_rating.append(movie_detail)
            # Now  i again do the same append them accordingly
            movies_detail = store.find('span', class_='sc-b189961a-8 hCbzGp cli-title-metadata-item').text
            movie_year.append(movies_detail)
    else:
        print("Error in parsing the data")
def save_to_csv(movie_name, movie_year, movie_rating, file_name):
    if soup != 'Error':
        dict = {'Rank and Name': movie_name, 'Ratings': movie_rating, 'Year': movie_year}
        dp = pd.DataFrame(dict)
        print(dp)
        # Now i put the data in dict and then into panda dataframe and then to a csv file
        dp.to_csv(file_name, index=False)
    else:
        print("Error in code. Can't save the data to a csv file")
fectch_imdb_top_movie(url, headers)
parse_data(soup)
save_to_csv(movie_name, movie_year, movie_rating,'imdb_top_movies_file')