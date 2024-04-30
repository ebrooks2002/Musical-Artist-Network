# Import WikiAPI
import wikipediaapi
import pandas as pd
import csv
import os
import lyricsgenius
import re

# Set the language to English
wiki_wiki = wikipediaapi.Wikipedia('ArtistMap (ebrooks1@macalester.edu)', 'en', extract_format=wikipediaapi.ExtractFormat.WIKI) # put your email here
# Specify the title of the Wikipedia page you want to access
page = 'List of hip hop musicians'
# Token:
token = 'wTWCvqt8fyKW0_VoFGqAinfL1SdZWNOYr1iA0sW2FcrCAaEAbZTJARumEuCB6bvf'
def get_lyrics(song_title, artist_name):
    genius = lyricsgenius.Genius(token)
    genius.remove_section_headers = True  # Remove section headers (e.g., [Chorus]) from lyrics when returned
    genius.skip_non_songs = True  # Skip search results that aren't songs (e.g., interviews)
    
    song = genius.search_song(song_title, artist_name)
    if song:
        return song.lyrics
    return "Lyrics not found."

artist_list = wiki_wiki.page(page) # (name of the wiki page)
artist_list_strings = list(artist_list.links.keys()) 
titles = artist_list_strings # Titles of the articles 
article_map = {}

for title in titles:
  article_map[title] = None

# Create a new CSV file in this folder, according the genre we are looking at.
filepath = 'rappers.csv'
data = [['Title', 'Text']]
with open('rappers.csv', mode='w', newline='') as file: #change path name according to genre
    writer = csv.writer(file)
    writer.writerows(data)
    
df = pd.read_csv(filepath) # turn to data frame. (should already contain headers)

total_articles = len(titles)
chunk_size = 1
chunks_completed = 0

for i in range(0, total_articles, chunk_size):
    end_index = min(i + chunk_size, total_articles)  # Safely handle last chunk size
    for x in range(i, end_index):
        page = wiki_wiki.page(titles[x])
        title = page.title
        title_clean = re.sub(r"\s*\(rapper\)|\s*\(musician\)", "", title)
        genius = lyricsgenius.Genius(token)
        genius.remove_section_headers = True  # Remove section headers (e.g., [Chorus]) from lyrics when returned
        genius.skip_non_songs = True  # Skip search results that aren't songs (e.g., interviews)
        artist = genius.search_artist(title_clean, max_songs=5)
        if not artist:
            continue
        songs = [song.title for song in artist.songs]
        lyrics = [get_lyrics(song, title) for song in songs]
        lyrics = "".join(lyrics).strip()
        print(lyrics)
        df = df._append({'Title': page.title, 'Text': lyrics}, ignore_index=True)
    chunks_completed += 1
    df.to_csv(filepath, index=False)  # Save the DataFrame to CSV

