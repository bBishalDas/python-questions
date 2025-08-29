# first attempt
file = input("Enter file address: ")

with open(file, "r") as f:
    lines_count = len(f.readlines())
    f.seek(0)
    word_count = len(f.read().split())
    f.seek(0)
    character_count = len(f.read())   # ❌ don’t strip here

print(f"Word count of your file: {word_count}") 
print(f"Number of lines in the file: {lines_count}")  
print(f"Character count in the file: {character_count}")




# improved virsion-
# (for UX mainly) using input to obtain file name 
file=input("ender file address: ")

# openinh file and using the readed file like a variable
with open(file) as f:
    content=f.read()

# instead of reseting the cursor multipule times using the variable "content" for better efficiency.
word_count=len(content.split())
lines_count=content.count("\n") +1 if content!="" else 0 # counting the lines in the file, by counting new lines (\n)
charater_count=len(content)
   
# printing the values.
print(f"word count of your file: {word_count}") 
print(f"number of lines in the file: {lines_count}")  
print(f"the character count in the file: {charater_count}")