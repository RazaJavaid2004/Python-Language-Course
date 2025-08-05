str = input("Enter the String: ")

vowel = 0

for i in str:
    if i == 'A' or i == 'a' or i == 'E' or i == 'e' or i == 'I' or i == 'i' or i == 'O' or i == 'o' or i == 'U' or i == 'u':
        vowel += 1

print("Number of Vowels in Your String: ", vowel)