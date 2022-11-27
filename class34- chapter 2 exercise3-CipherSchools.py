# take two commo seperated input from user
# 1.) user's name , exaple - "Harshit"
# 2.) a single chracter , "H"

# output- 2 print lines
# 1.) user's name length
# 2.) count the chracter that user inputed (bonus : case insensitive count)


name, char = input("enter comma seperated name and chracter : ").split(",")
lower = name.lower()
char = char.lower().replace(" ", "")
print(f"length of your name is {len(name)}")
print(f"chracter count : {lower.count(char)}")  # case sensitive
# Harshit-harshit
# H-h
