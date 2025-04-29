
# filter(condition, collection) = return all elements that pass a condition
# Transcript

grades = [91, 87, 67, 76, 24, 54, 43 ,23 ,65]

passing_grades = list(filter(lambda grade : grade > 60, grades))

print(passing_grades)       