import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')
clean_df = df.dropna()
head = clean_df.head()

print(head)