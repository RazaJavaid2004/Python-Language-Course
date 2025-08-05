def printlist(list, idx = 0):
    if idx == len(list):
        return
    print(list[idx])
    printlist(list, idx + 1)

subjects = ["Urdu", "English", "Science", "Math"]
printlist(subjects)