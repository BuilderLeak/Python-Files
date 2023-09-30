import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [2.1, 3.2, 4.3, 5.4, 6.5]})

# Calculate the sum of column 'A'
sum_A = df['A'].sum()

# Calculate the sum of column 'B'
sum_B = df['B'].sum()

print("Sum of column A:", sum_A)
print("Sum of column B:", sum_B)