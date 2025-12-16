# Personal Information Manager

## Project Description

This is my first Python project 🎉. The **Personal Information Manager** is a simple console-based program that stores and displays personal information in a clean and formatted way. It demonstrates basic Python concepts such as variables, user input, loops, string formatting, and input validation.

---

## Setup and Installation Instructions

### Step 1: Install Python

1. Download Python from **python.org**.
2. During installation, make sure to check the option:

   * ✅ *Add Python 3.x to PATH*
3. Click **Install**.

### Step 2: Verify Installation

1. Open **Command Prompt**.
2. Run the following command:

   ```bash
   python --version
   ```
3. If Python is installed correctly, the version number will be displayed.

### Step 3: Set Up VS Code

1. Open **Visual Studio Code**.
2. Go to **Extensions**.
3. Search for **Python**.
4. Install **Python by Microsoft**.

---

## Project Technical Requirements

* Use variables to store at least **4 pieces of personal information**.
* Get user input for at least **2 pieces of information**.
* Display all information in a **nicely formatted output**.
* Use **comments** to explain the code.
* Handle **basic user input validation**.
* Use **string methods (f-strings)** to format output.

---

## Code Structure

```
personal_info.py
```

---

## Source Code

```python
# M. Lakshmi Pathi
# My first python project - Program that stores and displays personal information

print("-" * 40)
print("WELCOME!! - PERSONAL INFORMATION MANAGER")
print("-" * 40)

name = "Mangu Lakshmi Pathi"                       # Static name variable (string)
age = 21                                           # Static age variable (integer)
city = "Hyderabad"                                 # Static city variable (string)
hobby = "Playing cricket and learning new things"  # Static hobby variable (string)

print("Tell me about yourselves!")
print("-" * 30)

favorite_food = input("What is your favorite food - ")
while favorite_food == "":
    print("\nPlease enter your favorite food")
    favorite_food = input("What is your favorite food - ")

favorite_color = input("What is your favorite color - ")
while favorite_color == "":
    print("\nPlease enter your favorite color!")
    favorite_color = input("What is your favorite color - ")

age_in_months = age * 12

print("\n" + "-" * 30)
print("DISPLAY INFORMATION")
print("-" * 30)

print(f"Name  : {name}")
print(f"Age   : {age} years ({age_in_months} months)")
print(f"City  : {city}")
print(f"Hobby : {hobby}")

print()
print(f"Favorite Food  : {favorite_food}")
print(f"Favorite Color : {favorite_color}")

print("\n" + "-" * 40)
print("Thanks for using this program. GOODBYE!!")
print("-" * 40)
```

---

## Working Application

### Output Example

```
----------------------------------------
WELCOME!! - PERSONAL INFORMATION MANAGER
----------------------------------------
Tell me about yourselves!
------------------------------
What is your favorite food - Biryani
What is your favorite color - Blue

------------------------------
DISPLAY INFORMATION
------------------------------
Name  : Mangu Lakshmi Pathi
Age   : 21 years (252 months)
City  : Hyderabad
Hobby : Playing cricket and learning new things

Favorite Food  : Biryani
Favorite Color : Blue

----------------------------------------
Thanks for using this program. GOODBYE!!
----------------------------------------
```

---

## Technical Details

1. **Static Variables**
   Four variables (`name`, `age`, `city`, `hobby`) are defined with fixed values at the time of creation.

2. **Dynamic User Input**
   Two variables (`favorite_food`, `favorite_color`) take input from the user at runtime.

3. **Formatted Output**
   The program uses **f-strings** to display the information in a clean and readable format.

4. **Input Validation**
   A `while` loop is used to ensure that user input is not empty. If the input is empty, the program prompts the user again.

---

## Test Cases

### Test Case 1: Input Validation

* **Scenario**: User presses Enter without providing input.
* **Expected Result**: Program displays a message asking the user to enter the input and continues execution.

### Test Case 2: Successful Execution

* **Scenario**: User provides valid inputs.
* **Expected Result**: Program runs successfully and displays all personal information without errors.
