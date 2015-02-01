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

# Scientific computing imports
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Import other files in package
from models.Comment import Comment

# Prepare Data into mutli-dimensional vectors
comments = Comment.select()
texts = np.array([comment.text for comment in comments])
metadata = [comment.id for comment in comments]

# Convert a collection of text documents to a matrix of token counts
vectorizer = CountVectorizer(stop_words='english', lowercase=True)
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
np.savetxt('president_matrix.csv', final_array, fmt='%s', delimiter=',')
