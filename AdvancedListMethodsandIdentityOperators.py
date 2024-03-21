submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
# Task 1
completed = list(set(submitted) & set(attended))
print("these students both completed and attended:", completed)
# Task 2
if set(submitted) == set(attended):
    print("the list are identical ")
else:
    print("the list are not identical")
# Task 3 
attended = [item for item in attended if item in submitted]
print(attended)