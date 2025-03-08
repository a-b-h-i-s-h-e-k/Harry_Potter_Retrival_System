from flask import Flask, request, render_template
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import re

app = Flask(__name__)

# Load the data and the model (adjust paths as necessary)
hp1 = pd.read_csv('Harry Potter 1.csv', delimiter=';', encoding='latin1')
corpus = hp1['Sentence'].tolist()  # Assuming 'Sentence' is the column with text

hp2 = pd.read_csv('Harry Potter 2.csv', delimiter=';', encoding='latin1')
hp2.rename(columns={'Sentence,,,,,,': 'Sentence'}, inplace=True)
corpus = hp2['Sentence'].tolist()  # Defining the corpus as a list of sentences

hp3 = pd.read_csv('Harry Potter 3.csv', delimiter=';', encoding='latin1')
#hp3.rename(columns={'SENTENCE': 'Sentence'}, inplace=True)
corpus = hp3['SENTENCE'].tolist()  # Defining the corpus as a list of sentences

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(corpus)

# Define a search function
def search_query(query):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    top_indices = np.argsort(similarities)[::-1][:5]
    return [(corpus[i], similarities[i]) for i in top_indices]

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        results = search_query(query)
        return render_template('results.html', query=query, results=results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
