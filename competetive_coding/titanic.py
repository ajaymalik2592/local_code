import pandas as pd

df = pd.DataFrame({"col1": [x for x in range(10)], "col2" : [x + 10 for x in range(10)]})
print(df.describe())


missing_number = df.isnull().sum().sort_values(ascending=False)
missing_percent = ((df.isnull().sum()/df.isnull().count())*100).sort_values(ascending=False)



