temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Task 1
Week_2 = temperatures[7:14]
print(f"These are the teperatures for week 2:" ,Week_2 )

# Task 2 
high_temps = [item for item in temperatures if item > 100]
print(f"these temperatures are all over 100" ,high_temps)

# Task 3 
temperatures.reverse()
backwards = temperatures[4:10]
print (backwards)

