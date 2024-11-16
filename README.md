
# Musical Artist Network

The aim of this project is to explore the relationship between artists in a specific music genre.

We use artists' wikipedia articles as our way of comparing them to each other. Articles contain information like background, style, and the names of other artists, which can give us hints into what their music is like. By comparing this information across artists, we can find which artists are more similar to each other, allowing users to find new artists they'd like.

We utitlize **TF-IDF** vectors to represent music artists' wikipedia articles and **cosine similarity** to compare artists within specific music genres. TF-IDF, which stands for term frequency - inverse document frequency is a simple method to try to quantify the meaning of a text. It is a statistical measurment that measures the importants of a word in a document, based on its frequency in that document and its frequency in the corpus. For each word, a score is calculated, reflecting its importance in the document.

Cosine similarity is a simple method to find how close two vectors are to each other. To find cosine similarity, we find the dot product of the two vectors and then divide the dot product by product of the two vectors' lengths.
 Example code: 
 ```
def cosine_sim(X, Y):
    dot_product = np.dot(X, Y)
    norm_X = np.linalg.norm(X)
    norm_Y = np.linalg.norm(Y)
    cosine_similarity = dot_product / (norm_X * norm_Y)
    return cosine_similarity
```

---

## Installation Requirements

To get started, install the necessary dependencies using `pip`:

```bash
pip install plotly
pip install pandas
pip install python-louvain
pip install numpy
pip install scikit-learn
pip install wikipedia-api
```

---

## How to Run the Project

Follow these steps to generate the artist network:

### Step 1: Select a Genre List

1. Go to the [Wikipedia page containing lists of musicians by genre](https://en.wikipedia.org/wiki/Category:Lists_of_musicians_by_genre).
2. Choose a genre that interests you (e.g., "List of ambient music artists").

### Step 2: Update the Script

- Open the `title_text.py` script.
- In the script, locate the line:
  ```python
  page = 'List of ambient music artists'
  ```
  and replace `'List of ambient music artists'` with the title of the Wikipedia page you selected in Step 1.

### Step 3: Run the Script

Execute the `title_text.py` script. This will generate a CSV file containing the names of artists and their corresponding Wikipedia articles. The resulting CSV file will look something like this:

---


  <img width="550" height="400" alt="Screen Shot 2024-11-06 at 8 21 31 PM" src="https://github.com/user-attachments/assets/2992f975-4485-48aa-8533-bb86fdd2bc69">


---

### Step 4: Convert to Graph-Ready Format

- Open the `graph_ready.py` script.
- Assign the variable:
  ```python
  filepath = 'ambient_artists.csv'
  ```
  with the name of the CSV file you generated in Step 3.
  
- **Note**: Converting the CSV to a graph-ready format may take a while, especially if the genre has over 1000 artists. The time complexity of this step is **O(n²)** due to the pairwise comparison of TF-IDF vectors between artists.


### Step 5: Visualize the Graph
- Open `visualize.py` script.
- Make sure you are reading the csv file of the graph you'd like to visualize:
  ```df = pd.read_csv('ambient_artists_graph_ready.csv')```
- The result will look something like this:
---
  ![rappergraph](https://github.com/user-attachments/assets/5f0bbb69-9caf-45e9-ad18-4f279bf98d0e)

---

This workflow helps in constructing a meaningful network of artists within a genre, which can be visualized or analyzed further using graph algorithms. Enjoy exploring the musical artist network!
