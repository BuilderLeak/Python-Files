#Finding the mode (most common value) in a column of a dataframe
#Mode = the value that appears most frequently.
import pandas as pd
from statistics import mode

# Create a dataframe
df = pd.DataFrame({'A': [10, 5, 7, 3, 8, 2, 5, 7, 5, 8, 5, 5, 7, 5],
                   'B': [15, 8, 10, 12, 7, 6, 5, 7, 5, 8, 5, 5, 7, 5]})

# Find the mode value in column 'A'
mode_val = mode(df['A'])

print("Mode value in column A:", mode_val)