import lyricsgenius
import pandas as pd
token = 'wTWCvqt8fyKW0_VoFGqAinfL1SdZWNOYr1iA0sW2FcrCAaEAbZTJARumEuCB6bvf'


genius = lyricsgenius.Genius(token)

def get_lyrics(song_title, artist_name):
    genius = lyricsgenius.Genius(token)
    genius.remove_section_headers = True  # Remove section headers (e.g., [Chorus]) from lyrics when returned
    genius.skip_non_songs = True  # Skip search results that aren't songs (e.g., interviews)
    
    song = genius.search_song(song_title, artist_name)
    if song:
        return song.lyrics
    return "Lyrics not found."

df = pd.read_csv("rappers.csv")
print(df.shape)
df = df[df['Text'].str.len() >= 10000]
df = df[df['Text'].str.find("Wikipedia:") == -1]
df.to_csv("rappers_famous1.csv")
print(df.head())
print(df.shape)
#artist = genius.search_artist("Glokk40Spaz", sort="title")



