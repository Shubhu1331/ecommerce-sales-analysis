import pandas as pd

df = pd.read_csv("SampleSuperstore.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

# Feature Engineering
df['Profit_Margin'] = df['Profit'] / df['Sales'].replace(0, 1)

df['Discount_Impact'] = df['Sales'] * df['Discount']

df['Profit_per_Unit'] = df['Profit'] / df['Quantity'].replace(0, 1)


print("\nFeature Engineered Data Preview")
print(df[['Sales', 'Profit', 'Quantity', 'Profit_Margin', 'Discount_Impact', 'Profit_per_Unit']].head())