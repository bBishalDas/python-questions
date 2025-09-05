address=input("enter the file name: ")

with open(address) as f:
    file=f.read().split()

max_len=0
longest_word=""


for word in file:
    if len(word)>max_len:
        max_len=len(word)
        longest_word=word

print(f"the logest word is {longest_word} with {max_len} letters.")
