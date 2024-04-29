import lyricsgenius
token = 'wTWCvqt8fyKW0_VoFGqAinfL1SdZWNOYr1iA0sW2FcrCAaEAbZTJARumEuCB6bvf'
def get_lyrics(song_title, artist_name):
    genius = lyricsgenius.Genius(token)
    genius.remove_section_headers = True  # Remove section headers (e.g., [Chorus]) from lyrics when returned
    genius.skip_non_songs = True  # Skip search results that aren't songs (e.g., interviews)
    
    song = genius.search_song(song_title, artist_name)
    if song:
        return song.lyrics
    return "Lyrics not found."

genius = lyricsgenius.Genius(token)
artist = genius.search_artist("Glokk40Spaz", sort="title")
print(artist.songs)
# Example usage
lyrics = get_lyrics("So What", "Bladee")
