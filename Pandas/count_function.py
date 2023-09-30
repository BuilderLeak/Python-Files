import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, None, 3, 4, 5],
                   'B': [2.1, 3.2, 4.3, None, 6.5]})

# Count the non-null values in column 'A'
count_A = df['A'].count()

# Count the non-null values in column 'B'
count_B = df['B'].count()

print("Count of non-null values in column A:", count_A)
print("Count of non-null values in column B:", count_B)