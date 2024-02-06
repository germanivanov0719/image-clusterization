from PIL import Image
import os


def clusterize(cluster: list[str]) -> list[str]:
    for path in cluster:
        data = Image.open(os.path.join("./data/img", path)).getdata()
        N = len(data) // 9
        color_cluster_size = 256 / N ** (1 / 3)
        

    return [""]
