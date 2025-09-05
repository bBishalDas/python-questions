# vowels= ["a","e","i","o","u","A","E","I","O","U"]

# file=input("enter file name: ")

# with open(file) as f:
#     text=f.read().strip()

# sum=0

# for char in text:
    
#     if char in vowels:
#       char=1
#     else:
#        char=0
    
#     sum+=char

# print(f"the number of vowels in this file are: {sum}.")



vowels= ["a","e","i","o","u","A","E","I","O","U"]

file=input("enter file name: ")

with open(file) as f:
    text=f.read().strip()

char=0
for word in vowels:
    vowels = "aeiouAEIOU"
    count = sum(1 for char in word if word in vowels)


print(f"the number of vowels in this file are: {sum}.")