students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

name_of_student = students.pop(2)
grade_of_student = grades.pop(2)
activity_of_student = activities.pop(2)
final_list = str(name_of_student) + ", " + \
    str(grade_of_student) + ", " + str(activity_of_student)

print(final_list)
