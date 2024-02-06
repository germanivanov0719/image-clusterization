import os
from clusterize import clusterize

paths = os.listdir("./data/img")
clusters = [paths]
while done := True:
    for i in range(len(clusters)):
        if len(clusters[i]) >= 18:
            done = False
            clusters[i] = clusterize(clusters[i])
