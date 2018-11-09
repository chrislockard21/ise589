import pandas as pd

# Importing the datasets
supplier_df = pd.read_csv('3dhubs_suppliers.csv')
machines_df = pd.read_csv('3dhubs_suppliers_machines.csv')

print(supplier_df.shape)

counts = supplier_df['Country'].value_counts()

print('Total US Suppliers: ' + str(counts.loc['United States']))

# Find dormant suppliers
df_0 = supplier_df[(supplier_df['Number of Reviews'] == 0)]

print(len(df_0))

df_1 = df_0[['supplier ID', 'Activation Date']]

print(df_1)

# Method 2

supplier_df.set_index(['Number of Reviews'], inplace = True)
print(supplier_df.index)
sum(supplier_df.index == 0)
supplier_df.reset_index(inplace = True)
print(supplier_df.index)

# Merge the DFs
# Left join joins suppliers to machines dataframe
total_df = pd.merge(machines_df, supplier_df, on = 'supplier ID', how = 'left')
print(total_df.shape)

df_2 = total_df[(total_df['category'] == 'ABS/PLA') & (total_df['Country'] == 'United States')]

print(df_2)
print(df_2['supplier ID'].nunique())
print(df_2['Price (USD)'].mean())

df_3 = supplier_df[(supplier_df['manufacturing partners'] == 'Yes')]

print(len(df_3))

print(df_3['Country'].value_counts())

# Check outliers
import matplotlib.pyplot as plt
plt.hist(x=df_2['Price (USD)'], bins = 'auto')
plt.xlabel('Price')
plt.ylabel('Frequency')
# plt.show()

import seaborn as sbs
df_5 = total_df[['category', 'Price (USD)']]

fig, ax = plt.subplots(figsize = (10,10))
ax.set_yscale('log')
sbs.boxplot(x='category', y='Price (USD)', data=df_5, ax=ax, whis=1.5)
# plt.show()

print(total_df.columns)
total_df = total_df.drop(['supplier ID', 'printer', 'material', 'Registered Business', 'category', 'manufacturing partners'])
corr = total_df.corr(mothod='pearson')
corr = total_df.corr(mothod='spearman')
fig, ax = plt.subplots(figsize=(10,10))
sds.heatmap(corr, xticklabels-corr.columns, yticklabels=corr.columns, annot=True)

plt.yticks(rotation=0)
plt.xticks(rotation=90)
