import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import mplcursors

file_path = 'utility_solar.csv'
df = pd.read_csv(file_path, delimiter='\t')
fips_column = df['state_fips']

capacity_factor_columns = df['capacity_factor_average']

# sector_column = df['sector']


# sector_array = sector_column.to_numpy()

# colors = ['blue' if sector == 'ipp' else 'red' for sector in sector_array] # => red if sector = anything but ipp (will change as needed) 

fips_array = fips_column.to_numpy()
unique_fips = len(set(fips_array)) # => 88 

average_capacity = df.groupby('state_fips')['capacity_factor_average'].mean().sort_values(ascending=False)

fips_counts = fips_column.value_counts()

plt.bar(range(len(capacity_factor_columns)), capacity_factor_columns.values, width=0.4, label='ipp') # y => fips_counts => add color=colors arg if need codes



for i, label in enumerate(capacity_factor_columns.values): # => fips_counts.values
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




plt.xticks(range(len(capacity_factor_columns)), capacity_factor_columns.index, rotation=90) # => fips_counts, fips_counts.index
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)

plt.xlabel('FIPS')
plt.ylabel('Average Capacity Factor')
plt.title('Average Storage Capacity Factor Per FIP (United States)')
plt.yticks(rotation=90)


mplcursors.cursor(hover=True)

props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# plt.text(78, 39.5, 'blue = FIPs associated with IPPs', fontsize=14,
#         verticalalignment='top', bbox=props)


plt.show()

