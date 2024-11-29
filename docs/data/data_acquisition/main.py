import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_wine_data():
    data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', names=['class','alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium',
        'total_phenols', 'flavanoids', 'nonflavanoid_phenols',
        'proanthocyanins', 'color_intensity', 'hue',
        'od280/od315_of_diluted_wines', 'proline'])
    return data

if __name__ == "__main__":
    dataset = load_wine_data()
    print(dataset.head())