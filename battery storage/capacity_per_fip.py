import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import mplcursors

file_path = 'battery_storage.csv'
df = pd.read_csv(file_path, delimiter='\t')
fips_column = df['fips']
# print(fips_column)
capacity_columns = df['capacity']
# print(capacity_columns)
sector_column = df['sector']
# print(sector_column)

sector_array = sector_column.to_numpy()

colors = ['blue' if sector == 'ipp' else 'red' for sector in sector_array] # => red if sector = anything but ipp (will change as needed) => add color index

fips_array = fips_column.to_numpy()
unique_fips = len(set(fips_array)) # => 88 

average_capacity = df.groupby('fips')['capacity'].mean().sort_values(ascending=False)

fips_counts = fips_column.value_counts()

plt.bar(range(len(average_capacity)), average_capacity.values, width=0.4, color=colors) # y => fips_counts 



for i, label in enumerate(average_capacity.values): # => fips_counts.values
    plt.annotate(
        f'', # => {fips_counts.index[i]}: #{label} => Cap: {label:.2f}
        (i, label),
        xytext=(0, 5),
        textcoords='offset points',
        ha='center',
        fontsize=8,
        color='black',
        weight='bold'
    )




plt.xticks(range(len(average_capacity)), average_capacity.index, rotation=90) # => fips_counts, fips_counts.index
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)

plt.xlabel('FIPS')
plt.ylabel('Average Capacity')
plt.title('Average Storage Capacity Per FIP (United States)')
plt.yticks(rotation=90)


mplcursors.cursor(hover=True)

plt.show()
