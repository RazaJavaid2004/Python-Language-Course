student = {
    "Name" : "Muhammad Raza",
    "CGPA" : 4.0,
    "isAdult" : True,
    "Subjects" : ["OOP", "DS", "DIC", "LDST", "PS"],
    "Hobbies" : ("FootBall", "Cricket", "Table Tennis"),
    "Age" : 19
}

print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))
print(student.get("Name"))

new = {"Father Name" : "Javaid Ali"}
student.update(new)
print(student)

student.update({"University" : "NEDUET"})
print(student)