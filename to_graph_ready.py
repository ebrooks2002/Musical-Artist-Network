import pandas as pd
import wikipediaapi
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
import sys
import re
import os

# The only part of this you change is line 12 and line 88.

filepath = 'ambient_artists.csv' #MUST CHANGE !!!!!!

# Put texts and titles into their own lists.
texts = []
titles = []
df = pd.read_csv(filepath)

for text, title in zip(df['Text'], df['Title']):
    if (type(text) != str) or (len(text) < 500):
      continue
    texts.append(text)
    titles.append(title)

# create object
tfidf = TfidfVectorizer()
tfidf_vectorizer = TfidfVectorizer(stop_words='english')

# get tf-df values
tfidf_matrix = tfidf.fit_transform(texts) # compute the tf-idf scores
dense_tfidf_matrix = tfidf_matrix.toarray()

# Using cosine similarity, we'll find which articles share similar tf-idf matrices.
def cosine_sim(X, Y):
    dot_product = np.dot(X, Y)
    norm_X = np.linalg.norm(X)
    norm_Y = np.linalg.norm(Y)
    cosine_similarity = dot_product / (norm_X * norm_Y)
    return cosine_similarity

cosine_sim_matrix = cosine_similarity(dense_tfidf_matrix)
csm_dict = {}
sum = 0
count = 0
for x in range(len(cosine_sim_matrix)):
  rapper1 = titles[x]
  for y in range(len(cosine_sim_matrix)):
    rapper2 = titles[y]
    if cosine_sim_matrix[x][y] == 1:
      continue
    both = f'{rapper1}/{rapper2}'
    csm_dict[both] = cosine_sim_matrix[x][y]
    sum += cosine_sim_matrix[x][y]
    count += 1

# Creating our CSV file to be turned into a our graph representation.
# Setting our threshold:
threshold = 0.2
# Initialize:
headers = ["Artist 1", "Artist 2", "Cosine Similarity"]
# Preallocating space in the dataframe:
num_rows = 18774071
df = pd.DataFrame(index=np.arange(num_rows), columns=headers)
def split_at_slash(text):
    # Regular expression to split at the first occurrence of '/'
    pattern = r"(.+?)/(.+)"

    # Using re.search to find the two parts of the string
    match = re.search(pattern, text)
    if match:
        return match.groups()  # Returns a tuple containing the two parts
    else:
        return text, ""  # Returns the original text and an empty string

i = 0
for key, value in csm_dict.items():
  if value > threshold:
    first_rapper, second_rapper = split_at_slash(key)
    df.iloc[i] = [first_rapper, second_rapper, value]
    i += 1
  else:
    pass

cleaned_df = df.dropna(how='all')
print(cleaned_df.columns)

cleaned_df.to_csv("ambient_artists_graph_ready.csv", index=False) # MUST CHANGE !!!!!!!
