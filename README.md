"# Harry_Potter_Retrival_System" 

Information Retrieval Project: Harry Potter Data Analysis
Overview
This repository contains the code and data for a project focused on building an information retrieval and text classification system using datasets from the Harry Potter universe. The primary goal was to implement various methods for information retrieval, query expansion, and try using transformers for such task. Additionally, this project explores two approaches: manual preprocessing and query expansion (using Harry_Potter.ipynb) and transformer-based classification (using Harry_transformers.ipynb).

Repository Structure
1. Harry_Potter/
Folder containing the main datasets in CSV format:

Harry Potter 1.csv
Harry Potter 2.csv
Harry Potter 3.csv
Potions.csv
Spells.csv
2. Structured_and_inverted/
Folder containing structured versions of the processed datasets in JSON format and the inverted index:

structured_corpus.json
structured_corpus_df2.json
structured_corpus_df3.json
structured_corpus_df4.json
structured_corpus_df5.json
inverted_index.json
3. App_outcomes/
Folder containing images showcasing various outputs of the app:

Query1.PNG, Query2.PNG, Query3.PNG: Examples of query results.
4. Code/
Folder containing the main code files:

Harry_Potter.ipynb: Jupyter notebook with traditional IR approaches.

Harry_transformers.ipynb: Jupyter notebook implementing transformer-based text classification using the HuggingFace library.

app.py: Python script for the Flask application providing an interactive retrieval system.

templates/index.html: HTML template for the Flask app’s interface.

templates/results.html: Results display page for the query system.

How to Run the Code
Running Harry_Potter.ipynb in Google Colab:
Open the Harry_Potter.ipynb notebook in Google Colab.
Create a folder named Harry_Potter in the Colab environment and upload all the CSV datasets into this folder.
Execute.
Running Harry_transformers.ipynb:
Open the Harry_transformers.ipynb and ensure the right paths for your data if you are working locally.
Execute.
Running the Flask App Locally:
Ensure Python and Flask are installed on your system.
Navigate to the Code directory in your terminal.
Run the Flask application:
python app.py
