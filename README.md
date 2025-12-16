#DOCUMENTATION
Project - PERSONAL INFORMATION MANAGER

Project Description
This is my first python project! It’s a program that stores and displays personal information.

Setup and installation instructions
•	Download and install Python from python.org
•	While installing, make sure to check the box
•	Add python to 3.x to PATH
•	Then, Click INSTALL.
•	Verify Installation
- Open Command Prompt and run command
       python -- version
•	Set up VS Code with Python extension.
- Open VS Code
- Go to Extensions
- Search “Python”
- Install “Python” by Microsoft

Project Technical Requirements
•	Use variables to store at least 4 pieces of personal information.
•	Get user input for at least 2 pieces of information.
•	Display all information in a nicely formatted output.
•	Use comments to explain what each part of your code does.
•	Handle basic user input validation.
•	Use string methods to format the output.

Code Structure
   - personal_info.py
# M. Lakshmi Pathi
# My first python project - Program that stores and displays personal information
print("-"*40)
print("WELCOME!! - PERSONAL INFORMATION MANAGER")
print("-"*40)
name="Mangu Lakshmi Pathi"                       # created a name variable and data as static, string as input.
age=21                                           # created an age variable and data is static, int as input.
city="Hyderabad"                                 # created a city variable and data is static, string as input.
hobby="Playing cricket and learning new things"  # created a hobby variable and data is static, string as input.
print("Tell me about yourselves!")
print("-"*30)
favorite_food = input("What is your favorite food - ")
while favorite_food=="":
    print()
    print("Please enter your favorite food")
    favorite_food=input("What is your favorite food - ")
favorite_color=input("What is your favorite color - ")
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
print("Thanks for using this program. GOODBYE!!")
print("-"*40)

Technical Details
- In this section, I will explain how I met the technical requirements.
1. I used four static variables. For these four static variables, we will give input at the time of variable creation only. These are fixed variables.(static)
2. And also, I used two variables for dynamic input. For these, input is given by the user at the time of run-time.(dynamic)
3.To display all the information in a neat manner, to give as an output, I used string methods using f-string.
4.Also, to handle basic user input validation, I used while loop. Which will help me in checking whether the  input is given or not. If not given, while loop will check and show a message to enter the input to the user.
