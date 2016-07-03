"""
Use TruncatedSVD
"""
# Basic Imports
import os
from pprint import pprint

import csv
from itertools import *
from operator import itemgetter

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import rand

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD

from matplotlib.pyplot import figure, show

from itertools import *
from operator import itemgetter

# Scientific computing imports
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
from scipy import sparse

# Import other files in package
from models.Comment import Comment

# Prepare Data into mutli-dimensional vectors
vectorizer = CountVectorizer()
lsa = TruncatedSVD(3)

comments = Comment.select()
texts = np.array([comment.text for comment in comments])
metadata = [comment.id for comment in comments]

vectors = vectorizer.fit_transform(texts)

# Transform data into two dimensions using LSA
X = lsa.fit_transform(vectors)

# Plot
x = X[:,0]
y = X[:,1]

import mpld3

fig, ax = plt.subplots(subplot_kw=dict(axisbg='#EEEEEE'))
N = 100

scatter = ax.scatter(x,
                     y,
                     # c=colors,
                     # s=1000 * np.random.random(size=N),
                     alpha=0.3,
                     cmap=plt.cm.jet)


ax.grid(color='white', linestyle='solid')

ax.set_title("Comments Clustering", size=21)

# tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
# mpld3.plugins.connect(fig, tooltip)

for i, txt in enumerate(metadata):
  ax.annotate(txt, (x[i],y[i]), size=5) 

# mpld3.save_html(fig, open('scatter.html','w'))

mpld3.show()
