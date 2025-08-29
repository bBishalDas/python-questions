# first virsion
original=input("enter file address you want to dublicate: ")
duplicate=input("enter the name you want 'dublicate file' to be: ")

with open(original, "r") as f:
    original_content=f.read()

with open(duplicate, "w") as h:
        h.write(original_content)

print(f"File '{original}' copied successfully as '{duplicate}' ✅")



# improved virsion 
original=input("enter file address you want to dublicate: ")
duplicate=input("enter the name you want 'dublicate file' to be: ")

# opens file by single "with" code as well as it is more reliable 
# for larger files as it prints the contents of the file line-by-line.
with open(original, "r") as f, open(duplicate, "w") as h:
    for lines in f:
         h.write(lines)

print(f"File '{original}' copied successfully as '{duplicate}' ✅")
