# delete all occurance of a specific char in a given string

s="delete all occurance of a specific char in a given string"
a= input("enter the char you want to remove")
new_s=""
for i in s:
    if i.lower() == a.lower():
        continue
    new_s = new_s+i
print(new_s)