import pandas as pd

data = {
  "Calories": [420, 380, 390],
  "Duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print(df.to_string()) 
