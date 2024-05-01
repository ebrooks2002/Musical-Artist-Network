# Authors: Ethan Brooks
''' 
This python script uses the wikipedia api to fetch links from a list of musicians from a genre, and then adds the titles and text contained within those links
to a csv file containing 2 columns: 'title' and 'text'
'''

# Import necessary libraries
import wikipediaapi
import pandas as pd
import csv

# Set the language to English
wiki_wiki = wikipediaapi.Wikipedia('ArtistMap (ebrooks1@macalester.edu)', 'en', extract_format=wikipediaapi.ExtractFormat.WIKI) # put your email here

# Specify the title of the Wikipedia page you want to access
page = 'List of ambient music artists'
artist_list = wiki_wiki.page(page) # (name of the wiki page)
artist_list_strings = list(artist_list.links.keys()) 
titles = artist_list_strings # Titles of the articles 
article_map = {}

for title in titles:
  article_map[title] = None

# Create a new CSV file in this folder, according the genre we are looking at.
filepath = 'ambient_artists.csv'
data = [['Title', 'Text']]
with open('ambient_artists.csv', mode='w', newline='') as file: #change path name according to genre
    writer = csv.writer(file)
    writer.writerows(data)
    
df = pd.read_csv(filepath) # turn to data frame. (should already contain headers)

total_articles = len(titles)
chunk_size = 100
chunks_completed = 0

for i in range(0, total_articles, chunk_size):
    end_index = min(i + chunk_size, total_articles)  # Safely handle last chunk size
    for x in range(i, end_index):
        page = wiki_wiki.page(titles[x])
        title = page.title
        text = page.text
        if ("Wikipedia" in title) or (len(text) < 5000) or ("List" in title) or ("ambient" in title):
            continue
        df = df._append({'Title': page.title, 'Text': page.text}, ignore_index=True)
    chunks_completed += 1
    df.to_csv(filepath, index=False)  # Save the DataFrame to CSV

