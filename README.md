

# Musical Artist Network

This project utilizes **TF-IDF** vectors to represent music artists and **cosine similarity** to compare artists within specific music genres. By analyzing artists' Wikipedia pages, we can create a network of musicians that highlights their similarities.

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

Execute the `title_text.py` script. This will generate a CSV file containing the names of artists and their corresponding Wikipedia articles. The resulting CSV file will look like this:

---

<div align="center">
  <img width="550" height="400" alt="Screen Shot 2024-11-06 at 8 21 31 PM" src="https://github.com/user-attachments/assets/2992f975-4485-48aa-8533-bb86fdd2bc69">
</div>

---

### Step 4: Convert to Graph-Ready Format

- Open the `graph_ready.py` script.
- Assign the variable:
  ```python
  filepath = 'ambient_artists.csv'
  ```
  with the name of the CSV file you generated in Step 3.
  
- **Note**: Converting the CSV to a graph-ready format may take a while, especially if the genre has over 1000 artists. The time complexity of this step is **O(n²)** due to the pairwise comparison of TF-IDF vectors between artists.

---

### Step 5: Visualize the Graph
- Open `visualize.py` script.
- Make sure you are reading the csv file of the graph you'd like to visualize:
  ```df = pd.read_csv('ambient_artists_graph_ready.csv')```
- The result will look something like this: 
This workflow helps in constructing a meaningful network of artists within a genre, which can be visualized or analyzed further using graph algorithms. Enjoy exploring the musical artist network!
