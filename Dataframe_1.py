
# pip install pandas(create dataframes), All array must have same length.
# pip install tabulate (display table in terminal) 

import pandas as pd

#Create data frame name 'employees' 
employees = pd.DataFrame({
    'employee_id' : [None, None, 1188, 1189, 7790],
    'office': [None,None, 'West-123', 'West-987', 'East-417'],
    'device_id': ['a897b209c326', 'd620e5741957', 'g164h566i795', 'h784i120j837', None]
})

#Create data frames name 'machines'
machines = pd.DataFrame({
    'device_id': ['a897b209c326', 'd620e5741957', 'g164h566i795', 'h784i120j837'],
    'operating_system': ['OS1', 'OS1', 'OS2', 'OS1']
})

# Display the first 5 rows of employees
print(employees.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types of employees
print(employees.info())

# Display the first 5 rows of machines
print(machines.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types of machines
print(machines.info())