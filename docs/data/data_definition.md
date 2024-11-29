# **Definición de los Datos**

## **Origen de los Datos**
Los datos provienen de un análisis químico realizado sobre vinos cultivados en la misma región de Italia, derivados de tres variedades diferentes. El propósito del análisis fue determinar la cantidad de 13 constituyentes encontrados en cada tipo de vino. Los datos se obtuvieron de la base de datos de la UCI Machine Learning Repository, específicamente del conjunto de datos "Wine".

- **Fuente**:  
  - [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data)
  - Descripción: El dataset fue proporcionado por Riccardo Leardi de la Universidad de Génova.

## **Especificación de los Scripts para la Carga de Datos**
El proceso de carga de datos se realiza utilizando un script Python que descarga los datos desde el repositorio de UCI y luego los carga en un DataFrame de `pandas`. A continuación, se muestra el script básico para la carga de los datos:

```python
import pandas as pd

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'
column_names = ['class','alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 'magnesium', 
                'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 'proanthocyanins', 
                'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline']

data = pd.read_csv(url, names=column_names)

print(data.head())