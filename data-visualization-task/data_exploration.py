# data_exploration.py
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

print("=" * 50)
print("DATA EXPLORATION - Restaurant Tips Dataset")
print("=" * 50)

# Load a built-in dataset from seaborn
print("\n📊 Loading dataset...")
df = sns.load_dataset('tips')

# Basic exploration
print("\n📋 FIRST 5 ROWS OF DATA:")
print(df.head())

print("\n📋 LAST 5 ROWS OF DATA:")
print(df.tail())

print("\n📊 DATASET INFORMATION:")
print(df.info())

print("\n📈 BASIC STATISTICS:")
print(df.describe())

print("\n🔍 COLUMN NAMES:")
print(df.columns.tolist())

print("\n🔢 MISSING VALUES CHECK:")
print(df.isnull().sum())

print("\n📊 UNIQUE VALUES IN CATEGORICAL COLUMNS:")
for col in df.select_dtypes(include=['object']).columns:
    print(f"{col}: {df[col].unique()}")

print("\n" + "=" * 50)
print("✅ Data exploration complete!")
print("=" * 50)