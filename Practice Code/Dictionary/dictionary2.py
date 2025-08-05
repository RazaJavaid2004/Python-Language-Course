# nested dictionary

student = {
    "Name" : "Muhammad Raza",
    "CGPA" : 4.0,
    "isAdult" : True,
    "Subjects" : {
        "Chem" : 98,
        "Physics" : 99,
        "Math" : 100
    },
    "Hobbies" : ("FootBall", "Cricket", "Table Tennis"),
    "Age" : 19
}

print(student)
print(student["Subjects"])
print("Math: ", student["Subjects"] ["Math"])

student["Subjects"] ["Physics"] = 100
print("Physics: ", student["Subjects"] ["Physics"])