import pandas as pd 

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'

df = pd.read_csv(url, header=None)

df["new_column"] = df[5].apply(lambda x: x*2)

print("Columns:\n", df.columns)
print("Head:\n", df.head())
print("Shape:\n", df.shape)