# graph of n centroids

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans 

data = pd.read_csv('link_of_data')

clusters = []

max_iter = 10
#you need to know max_iter before
#can be test the max_iter for a lot of values

for i in range(1, max_iter + 1):
    kmeans = KMeans(n_clusters=i, random_state=1234)
    kmeans.fit(data)
    clusters.append((i,kmeans.inertia_,))
plt.plot([t[0] for t in clusters],[t[1] for t in clusters], marker="X")

#elbow_cluster = the best num of clusters
