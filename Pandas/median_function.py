#Median = the value in the middle, after you have sorted all values ascending.
import pandas as pd

# Create a dataframe
df = pd.DataFrame({'A': [10, 5, 7, 3, 8, 2],
                   'B': [15, 8, 10, 12, 7, 6]})

#2-3-5-7-8-10
# Find the median value in column 'A'
median_valA = df['A'].median()
# Find the median value in column 'B'
median_valB = df['B'].median()

print("Median value in column A:", median_valA)
print("Median value in column B:", median_valB)