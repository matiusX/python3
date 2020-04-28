import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import seaborn as sns
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# elbow_cluster = 15
# setting a var for n of clusters:
num_clusters = 15

agglomerative_model = AgglomerativeClustering(n_clusters=num_clusters)
model = KMeans(n_clusters=num_clusters)
scaler = StandardScaler()
tsne = TSNE()

# accessing database
uri = 'https://raw.githubusercontent.com/alura-cursos/machine-learning-algoritmos-nao-supervisionados/master/movies.csv'
data = pd.read_csv(uri)


# rename columns in database
def personalize_films(database):
    new_names = {
        'movieId': 'id',
        'genres': 'gen'
    }
    database = database.rename(columns=new_names)
    return database


# a function to create a graph of genres
def create_graph(to_fit, f_model):
    graph = tsne.fit_transform(to_fit)
    sns.set(rc={'figure.figsize': (13, 13), })

    seq_colors = ['#000000', '#ff0000', '#00ff00', '#0000ff', '#646400', '#006464', '#a1a1a2', '#ffff64', '#00ffff',
                  '#ff00ff', '#8701fd', '#ff7e69', '#ff5729', '#52648c', '#53032d']
    return sns.scatterplot(x=graph[:, 0],
                           y=graph[:, 1],
                           hue=f_model.labels_,
                           palette=sns.color_palette(seq_colors, num_clusters),
                           )


data = personalize_films(data)

# creation of binary genres
raw_genres = data.gen.str.get_dummies()
films_features = pd.concat([data, raw_genres], axis=1)
# scaling genres
genres = scaler.fit_transform(raw_genres)
model.fit(genres)

# Creating centroids
centroids = pd.DataFrame(model.cluster_centers_,
                         columns=raw_genres.columns)
centroids.transpose().bar(subplots=True,
                          figsize=(25, 50),
                          sharex=False,
                          rot=0)

matriz_distancia = linkage(centroids)
dendrograma = dendrogram(matriz_distancia)
plt.show()

create_graph(genres, model)
plt.show()
