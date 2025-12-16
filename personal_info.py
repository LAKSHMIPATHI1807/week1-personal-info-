# M.Lakshmi Pathi
# My first python project - Program that stores and displays personal information

print("-"*40)
print("WELCOME!! - PERSONAL INFORMATION MANAGER")
print("-"*40)


name="Mangu Lakshmi Pathi"                       # created a name variable and data as static,string as input.
age=21                                           # created a age variable and data is static, int as input.
city="Hyderabad"                                 # created a city variable and data is static, string as input.
hobby="Playing cricket and learning new things"  # created a hobby variable and data is static, string as input.

print("Tell me about yourselves!")

print("-"*30)

favorite_food = input("What is your favorite food - ")
while favorite_food=="":
    print()
    print("Please enter your favorite food")
    favorite_food=input("What is your favorite food - ")
    
favorite_color=input("What is your favorite colour - ")
while favorite_color=="":
    print()
    print("Please enter your favorite color!")
    favorite_color=input("What is your favorite color - ")
    
age_in_months = age*12

print()
print("-"*30)
print("DISPLAY INFORMATION")
print("-"*30)
    
print(f"Name  : {name}")
print(f"Age   : {age} years ({age_in_months}months)")
print(f"City  : {city}")
print(f"Hobby : {hobby}")

print()

print(f"Favorite Food  : {favorite_food}")
print(f"Favorite Color : {favorite_color}")

print()

print("-"*40)
print("Thanks for using this program.GOODBYE!!")
print("-"*40)