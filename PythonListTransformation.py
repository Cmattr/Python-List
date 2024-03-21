# Task 1 
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort ()
grades.reverse()

#Task 2

average = sum(grades) / len(grades)
print (f"{average} is the average grade")

# Task 3 

print(grades)
failingGrades = [item for item in grades if item < 80]
print(f"{failingGrades} failed")
