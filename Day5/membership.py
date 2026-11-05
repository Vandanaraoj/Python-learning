#Membership operator
# name8='Vandana'
# if'a' in name8:
#     print("A is present in the string")

# text="Python is a programming language"
# print("Python" in text)
# print("Java"  not in text)
# print(text in 'aeiou')

#Using for loop
name9= "Vandana"
for i in range(len(name9)):
   if name9[i] in 'aeiou':
    print(f"{name9[i]} is a vowel")
   else:
    print(f"{name9[i]} is not a vowel")