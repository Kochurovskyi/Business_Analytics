import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import TruncatedSVD

def plot(x,y,cl):
    plt.figure(figsize=(10,10))
    for i in range(len(Y)):
        if cl[i] == 0: clr = 'blue'
        if cl[i] == 1: clr = 'green'
        if cl[i] == 2: clr = 'red'
        if cl[i] == 3: clr = 'black'
        plt.scatter(feat[i, 0], feat[i, 1], c=clr)
        plt.text(feat[i, 0], feat[i, 1], y[i], fontsize=6, c=clr)
    plt.show()

df = pd.read_csv('Cities.csv', index_col='No.')
Y = np.array(df.City)
x = np.array(df.drop(columns=['City']))
model = KMeans(n_clusters=4, random_state=0)
#model = AgglomerativeClustering(n_clusters=4)

#pred = model.fit_predict(x)

svd = TruncatedSVD(n_components=2, random_state=0)
feat = svd.fit_transform(x)
pred = model.fit_predict(feat)

plot(feat, Y, pred)