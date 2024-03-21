students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Task 1
students_combined = zip(students, grades, activities)
filtered_students = [(name, grade, activity) for name, grade, activity in students_combined if grade < 80]
print(filtered_students)

# Task 2 
students_approved = ["John", "Doe", "Smith"]

# Task 3
print (students_approved)

