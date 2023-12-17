import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import mplcursors

file_path = 'battery_storage.csv'
df = pd.read_csv(file_path, delimiter='\t')
fips_column = df['fips']
# print(fips_column)


fips_array = fips_column.to_numpy()
unique_fips = len(set(fips_array)) # => 88 


fips_counts = fips_column.value_counts()

plt.bar(range(len(fips_counts)), fips_counts.values, width=0.25)

for i, label in enumerate(fips_counts.values):
    plt.annotate(
        f'#{label}', #{fips_counts.index[i]}: #{label}
        (i, label),
        xytext=(0, 5),
        textcoords='offset points',
        ha='center',
        fontsize=8,
        color='black',
        weight='bold'
    )


# Set x-axis labels to be the FIPS codes
plt.xticks(range(len(fips_counts)), fips_counts.index, rotation=90)
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)

plt.xlabel('FIPS')
plt.ylabel('Count')
plt.title('FIPS Counts')
plt.yticks(rotation=90)


mplcursors.cursor(hover=True)
plt.show()
