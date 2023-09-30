import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [2.1, 3.2, 4.3, 5.4, 6.5]})

# Calculate the mean of column 'A'
mean_A = df['A'].mean()

# Calculate the mean of column 'B'
mean_B = df['B'].mean()

print("Mean of column A:", mean_A)
print("Mean of column B:", mean_B)
