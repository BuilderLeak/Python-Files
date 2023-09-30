import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 25, 30],
        'City': ['New York', 'Los Angeles', 'Chicago', 'New York', 'Chicago'],
        'Salary': [50000, 60000, 55000, 45000, 70000]}
df = pd.DataFrame(data)

# Grouping by 'City'
grouped_city = df.groupby('City')

# Calculating mean of 'Age' and sum of 'Salary' for each city
mean_age = grouped_city['Age'].mean()
sum_salary = grouped_city['Salary'].sum()

# Printing the results
print("Mean Age by City:")
print(mean_age)

print("\nSum of Salary by City:")
print(sum_salary)

# Printing city-wise names
def get_names(group):
    return group['Name'].tolist()

city_names = grouped_city.apply(get_names)
print("\nCity-wise Names:")
print(city_names)

# writing dataframe as in excel file
writer = pd.ExcelWriter('output.xlsx')  
df.to_excel(writer)  
writer.save()  
print('DataFrame is written successfully to the Excel File.')  

print(df)