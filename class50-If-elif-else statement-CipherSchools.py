# if elif statement
# show ticket pricing
# 1 to 3 (free)
# 4 to 10 (150)
# 10 to 60 (250)
# above 60 (200)
age = input("Enter your age: ")
age=int(age)
if 0<age<=3:
    print("Your ticket price is free")
elif 3<age<=10:
    print("Your ticket price is 150")
elif 10<age<=60:
    print("Your ticket price is 250")
else:
    print("Your ticket price is 200")
