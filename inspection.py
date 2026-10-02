import pandas as pd
import numpy as np

# Load datasets
df_a = pd.read_csv("TABLE1_BasicLiteratePopulation.csv")
df_b = pd.read_csv("TABLE2_LiteracyLevel5Above.csv")
df_c = pd.read_csv("TABLE3_FunctionalLiteratePopulation.csv")
df_d = pd.read_csv("TABLE2_LiteracyLevel10Above.csv")

# Inspect dataset A
print("Dataset A:", df_a.shape)
print(df_a.head())
print(df_a.dtypes)
print(df_a.isnull().sum())
print("Duplicates:", df_a.duplicated().sum())

# Inspect dataset B
print("Dataset B:", df_b.shape)
print(df_b.head())
print(df_b.dtypes)
print(df_b.isnull().sum())
print("Duplicates:", df_b.duplicated().sum())

# Inspect dataset C
print("Dataset C:", df_c.shape)
print(df_c.head())
print(df_c.dtypes)
print(df_c.isnull().sum())
print("Duplicates:", df_c.duplicated().sum())

# Inspect dataset C
print("Dataset D:", df_d.shape)
print(df_d.head())
print(df_d.dtypes)
print(df_d.isnull().sum())
print("Duplicates:", df_d.duplicated().sum())