import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('QueryResults.csv',names=['DATE','TAG','POSTS'],header=0)
print(df.head())