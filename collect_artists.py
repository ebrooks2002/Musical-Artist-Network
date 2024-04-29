import pandas as pd
import lyricsgenius
import wikipediaapi
import csv

wiki_wiki = wikipediaapi.Wikipedia('ArtistMap (ebrooks1@macalester.edu)', 'en', extract_format=wikipediaapi.ExtractFormat.WIKI) # put your email here
page = 'List of Hip Hop Musicians'

artist_list = wiki_wiki.page(page) # (name of the wiki page)
artist_list_strings = list(artist_list.links.keys()) 
titles = artist_list_strings # Titles of the articles

print(titles)

# Create a new CSV file in this folder, according the genre we are looking at.
filepath = 'music_genres_titles_text.csv'
data = [['Title', 'Text']]
with open('music_genres_titles_text.csv', mode='w', newline='') as file: #change path name according to genre
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
        df = df._append({'Title': page.title, 'Text': page.text}, ignore_index=True)
    chunks_completed += 1