import pandas as pd
from datetime import date

from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
  data = pd.read_csv("DonneesJuinAnonymise.csv")
  data = data.drop(["object", "info_end"], axis=1)
  data = data.dropna(axis=0)
  data = data.sort_values(by=['resource', 'timestamp (UTC)'])

  data['status + 1'] = data['status'].shift(-1)


  lasts = data.drop_duplicates(subset='resource', keep='last')

  data = data[~data.index.isin(lasts.index)]

  print(data)



