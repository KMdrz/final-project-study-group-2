import pandas as pd
import numpy as np

# Load datasets
df_a = pd.read_excel("TABLE1_BasicLiteratePopulation.xlsx", header=None)
df_b = pd.read_excel("TABLE2_LiteracyLevel5Above.xlsx", header=None)
df_c = pd.read_excel("TABLE3_FunctionalLiteratePopulation.xlsx", header=None)
df_d = pd.read_excel("TABLE4_LiteracyLevel10Above.xlsx", header=None)

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

# Inspect dataset D
print("Dataset D:", df_d.shape)
print(df_d.head())
print(df_d.dtypes)
print(df_d.isnull().sum())
print("Duplicates:", df_d.duplicated().sum())