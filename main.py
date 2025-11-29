import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('dataset.csv')

#pd.fillna()

print(df.describe())

df.isnull.sum()






