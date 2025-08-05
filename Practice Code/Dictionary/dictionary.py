# Keys can only be of immutable datatype

student = {
    "Name" : "Muhammad Raza",
    "CGPA" : 4.0,
    "isAdult" : True,
    "Subjects" : ["OOP", "DS", "DIC", "LDST", "PS"],
    "Hobbies" : ("FootBall", "Cricket", "Table Tennis"),
    "Age" : 19
}

print(student)

student["Name"] = "Raza Javaid"
student["Father Name"] = "Javaid Ali"

print(student)

print("Name: ", student["Name"])
print("GPA: ", student["CGPA"])