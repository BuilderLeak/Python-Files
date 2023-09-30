import pandas as pd

# Create a dataframe
df = pd.DataFrame({'A': [10, 5, 7, 3, 8, 2],
                   'B': [15, 8, 10, 12, 7, 6]})

# Find the minimum and maximum values in column 'A'
min_val = df['A'].min()
max_val = df['A'].max()

print("Minimum value in column A:", min_val)
print("Maximum value in column A:", max_val)
