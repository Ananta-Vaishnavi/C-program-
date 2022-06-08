#1.Create a dataframe which holds information of 15 students containing the information as (nested list) Name,RollNo,Age,marks of 3 different subjects.Perform the following operations
# Display the information of first 4 students
# Display the information of last 5 students.
# Display the names and age of all students.
# Display the details of students whose age 
is greater than 20.
# Calculate the class average score of marks of the students.
# Display the student information in ascending order of marks.
# Display the details of student who scored highest score .
# Display the details of Name,roll No and marks of student.
import pandas as pd
data={'Name':['James', 'Mary', 'Robert', 'Patricia', 'John', 'Jennifer', 'Michael', 'Linda','David', 'Elizabeth', 'William', 'Barbara', 'Richard', 'Susan', 'Joseph'],
  'RollNo':[10,11,21,22,32,41,33,52,44,54,19,93,85,76,86],
  'Age':[23, 20, 18, 23, 23, 29, 23, 20, 18, 19, 23, 23, 19, 19, 19],
  'marks':[70, 73, 76, 60,38, 77, 75, 79, 82, 85, 88, 91, 94, 97,69]}
ds=pd.DataFrame(data)
print(ds.head(4))
print(ds.tail())
print(ds.iloc[[0,2]])
print(ds.iloc[[0,1,3]])
print(ds[ds['Age']>20])
a=data['marks']
print(sum(a)/len(a))
print(ds[ds['marks']==max(a)])
print(ds.sort_values('marks'))
