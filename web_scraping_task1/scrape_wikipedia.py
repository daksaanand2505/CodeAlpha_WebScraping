import pandas as pd

# Load the scraped data
df = pd.read_csv('scraped_data/country_population.csv')

print("=" * 50)
print("📊 YOUR SCRAPED DATASET")
print("=" * 50)

print(f"\n✅ Total countries scraped: {len(df)}")
print(f"✅ Total columns: {len(df.columns)}")
print(f"\n📋 Column names: {list(df.columns)}")

print("\n🔍 FIRST 5 ROWS:")
print(df.head())

print("\n🔍 LAST 5 ROWS:")
print(df.tail())

print("\n📈 BASIC STATISTICS:")
print(df.describe())

print("\n🏆 TOP 10 MOST POPULOUS COUNTRIES:")
print(df.head(10))