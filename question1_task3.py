grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort()

grades.remove(72)
grades.remove(76)
grades.remove(78)

print(grades)

grades.insert(0, "Failed")
grades.insert(1, "Failed")
grades.insert(2, "Failed")

print(grades)
