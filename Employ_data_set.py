import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




df = pd.read_csv('D:/numpy/local_company_employees.csv')

print(df)
print('Missing values in each column:')
print(df.isnull().sum())

print(df["Gender"].value_counts())


df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['PerformanceRating'] = df['PerformanceRating'].fillna(df['PerformanceRating'].median())
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(df.mean(numeric_only=True), inplace=True)


# remove duplicates records

df.drop_duplicates(inplace=True)

# Replace negative salaries with NaN

df['Salary'] = df['Salary'].apply(lambda x: x if x >= 0 else np.nan)

Salary_mean = df['Salary'].mean()
salary_std = df['Salary'].std()
lower_bound = Salary_mean - 3 * salary_std
upper_bound = Salary_mean + 3 * salary_std

#remove row where salary is outside the range of mean ± 3*std

df = df[(df['Salary'] >= lower_bound) & (df['Salary'] <= upper_bound)]

df = df.dropna(subset=[
    'EmployeeID','Name','Age','Gender','Department','Designation','Salary','Experience','City','JoiningDate','PerformanceRating'
])

gender_count = df['Gender'].value_counts()

plt.figure(figsize=(8, 5))
plt.pie(
    gender_count.values,
    labels=gender_count.index,
    autopct='%1.1f%%',
    colors=['skyblue', 'lightcoral'],
    startangle=90,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

plt.title('Employees by Gender')
plt.tight_layout()
plt.savefig('D:/numpy/employee_gender_count.png')
plt.show()
Department_count = df['Department'].value_counts()
plt.bar(
    Department_count.index,
    Department_count.values,
    color=['green', 'red']
)

plt.title('Departmentr of Employees ')
plt.xlabel(' number of Department')
plt.ylabel('number of employees')
plt.grid(color='gray', linestyle=':', linewidth=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('D:/numpy/employee_Department_count.png')
plt.show()


# Average Salary by Department

department_salary = df.groupby('Department')['Salary'].mean()

plt.figure(figsize=(10, 5))

plt.bar(
    department_salary.index,
    department_salary.values,
    color='skyblue'
)

plt.title('Average Salary by Department')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.xticks(rotation=45)
plt.grid(color='gray', linestyle=':', linewidth=0.2)
plt.legend()
plt.tight_layout()
plt.savefig('D:/numpy/department_average_salary.png')
plt.show()



city_count = df['City'].value_counts()
plt.figure(figsize=(8, 5))

plt.pie(
    city_count.values,
    labels=city_count.index,
    autopct='%1.1f%%',
    colors=['blue', 'teal'],
    startangle=90,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

plt.title('City of Employees')
plt.tight_layout()
plt.savefig('D:/numpy/employee_city_count.png')
plt.show()


df.to_csv('D:/numpy/local_company_employees_cleaned.csv', index=False)
print('Data cleaning completed. Cleaned data saved to local_company_employees_cleaned.csv')











