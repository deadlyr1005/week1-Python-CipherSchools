name = "             Harshit             "
dots = "........................"
# lstrip() method
print(name + dots)
print(name.lstrip() + dots)
print(name.rstrip() + dots)
print(name.strip() + dots)
name = name.replace(" ", "")
dots = dots.replace(".", "1")
print(name)
print(dots)
