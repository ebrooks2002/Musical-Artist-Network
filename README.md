# Musical Artist Network
This half of the project utilizes TF-IDF vectors to represent artists, and then cosine similarity to compare artists within a music genre.

### Installation requirements: 
- Plotly: ```pip install plotly ```
- Pandas: ```pip install pandas ```
- Python-Louvain: ```pip install python-louvain```
- NumPy: ```pip install numpy```
- scikit-learn: ```pip install scikit-learn```
- wikipedia-api: ```pip install wikipediaapi```

### How to run:

- Go to this wikipedia page, which contains lists of musicians by genre: https://en.wikipedia.org/wiki/Category:Lists_of_musicians_by_genre
   <img width="700" alt="Screen Shot 2024-11-06 at 8 04 00 PM" src="https://github.com/user-attachments/assets/48185d94-0f00-4516-9954-3385d2c268a4">
- Select a list and type the article's title in title_text.py where it says: ```page = 'List of ambient music artists'```
- Run the titles_text.py script. This should produce a csv file containing the artists' names and their wikipedia articles that looks something like this:
  
  <img width="750" alt="Screen Shot 2024-11-06 at 8 21 31 PM" src="https://github.com/user-attachments/assets/2992f975-4485-48aa-8533-bb86fdd2bc69">

- 



