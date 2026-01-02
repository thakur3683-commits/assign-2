import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'HR'],
    'Salary': [45000, 54000, 50000, 62000, 47000]
}

df = pd.DataFrame(data)
df.head()
df[['Age', 'Salary']].describe()
df[df['Department'] == 'HR']['Salary'].mean()

df['Bonus'] = df['Salary'] * 0.10
df[(df['Age'] >= 25) & (df['Age'] <= 30)]

df.groupby('Department')['Salary'].mean()
sorted_df = df.sort_values(by='Salary')
sorted_df.to_csv('sorted_salary.csv', index=False)
