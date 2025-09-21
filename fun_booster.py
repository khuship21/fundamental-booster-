print("Welcome To The Interactive Personal Data Collector ")

name = input("please enter your name :  ")
age = int(input("please enter your age :"))
height = float(input("please enter your height :"))
number = int(input("please enter your favourite number :"))

print("thank you, here are the information we collected")

print("name:",name, ("type:", type(name), ("memory address:", id(name))))
print("age:",age, ("type:", type(age), ("memory address:", id(age))))
print("height:",height, ("type:", type(height), ("memory address:", id(height))))
print("number :",number , ("type:", type(number ), ("memory address:", id(number))))

print("your birth year is approximately: 2005 (based on your age of 21) ")
print("thank you for using the personal data collector")