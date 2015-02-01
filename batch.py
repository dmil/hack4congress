"""
Find form-emails and group emails by form.
"""

# Basic Imports
import os
from pprint import pprint
import numpy as np
import csv
from itertools import *
from operator import itemgetter
from blessings import Terminal

# Scientific computing imports
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
from scipy import sparse

# Import other files in package
from models.Comment import Comment
from models.Form import Form
from models.Email import Email

t = Terminal()

# Prepare Data into mutli-dimensional vectors
comments = Comment.select()
texts = np.array([comment.text for comment in comments])
metadata = [comment.id for comment in comments]

# Convert a collection of text documents to a matrix of token counts
vectorizer = CountVectorizer(lowercase=True)
count_vectors = vectorizer.fit_transform(texts)

# Calculate cosine similarity vectors
cosine_vectors = [cosine_similarity(v, count_vectors) for v in count_vectors]
cosine_vectors = np.vstack(cosine_vectors)

# Add vertical and horizontal axes
metadata_vector_x = np.array([metadata])
metadata_vector_y = np.array([[' '] + metadata]).transpose()
final_array = np.vstack((metadata_vector_x, cosine_vectors))
final_array = np.hstack((metadata_vector_y, final_array))

# Output to CSV
np.savetxt('similarity_matrix.csv', final_array, fmt='%s', delimiter=',')

# Find the batches
boolean_matrix = [map(lambda x: 1 if x > .9 else 0, vector) for vector in cosine_vectors]
g = nx.Graph(sparse.csr_matrix(boolean_matrix))

# Populate Forms
for batch in nx.connected_components(g):
  f = Form(blank="")
  f.save()
  # form.save(force_insert=True)
  for item_id in batch:

    if len(batch) <= 1: 
      continue

    item_id += 1

    try:
      comment = Comment.get(Comment.id==item_id)
      comment.form = f
      comment.save()
      # import pdb; pdb.set_trace()
      # comment.save(force_insert=True)
    except:
      print t.red("Could not get comment with id #%d" % item_id)
