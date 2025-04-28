====================================
My first Project of DataSense
====================================

- Create Virtual Enviornment
    - python -m venv firstproject (Command I used to create Virtual Envoirnment)
        - **python** - The Python interpreter, the program that runs Python code on your computer.
        - **-m** - A flag telling Python to run a module (a Python library or tool) as a script.
        - **venv** - A built-in Python module that creates isolated virtual environments for projects.
        - **firstproject** - The name of the folder where the virtual environment will be created for this project.
- Activate
    - Activated the virtual envoirnment by running this command **firstproject/Scripts/activate.ps1**
- Install Dependencies
    - In this step Install all the modules you require for this project like numpy,pandas etc
- Write Code


- Using Python 3.12.8

- Used 2 ways to use Emojis in the project
    - First method by using emoji library
        - Install emoji library using command **pip install emoji**
        - Import the library by using command **import emoji**
        - Use function **emojize** of library emoji to use the desired emoji.
    - Second Method, Press Windows + . and select the emoji you want to use at desired place (much simpler and easy to use)

- import time module to use the sleep function.

=====================================
Project Description
=====================================
- This project collects user inputs through a questionnaire, analyzes them to determine the user's personality type, and displays a personalized fun personality report based on the inputs.

=====================================
Functions used in project
=====================================
1 - **print()**
    - The print function in Python displays the output/desired lines to the user. It’s like telling the computer to write something on the screen.

2 - **input()**
    - The input function is used to take the input from the function. **By Default it treats the input as a string**.

3 - **int() and str()**
    - int function is used to convert the value like str or float into an integer. For ex- int("5") to 5.
    - str function is used to convert the value like a number to string. For ex- str(5) becomes "5".

4 - **title()**
    - title is a string method that capitalizes the first letter of each word in a string. For ex-, "hello world".title() returns "Hello World".

5 - **strip()**
    - strip is a string method that removes the leading and trailing whitespace characters like spaces,\t,\n etc from the string. For ex- "  Rohit Kaushik  ".strip() becomes "Rohit Kaushik".

6 - **upper() and lower()**
    - upper is a string method that converts a string into an Uppercase. For ex- "hello".upper() becomes "HELLO".
    - lower is is a string method that converts a string into an Lowercase. For ex- "HELLO".lower() becomes "hello".

7 - **len()**
    - The len function returns the number of items in an object, such as the length of a string, list, or tuple. For example, len("Hello") returns 5, counting the characters in the string.

8 - **sleep()**
    - sleep function from the time module, pauses program execution for a specified number of seconds. For example, time.sleep(2) delays the program for 2 seconds before continuing.

=====================================
Conditional Statement
=====================================
1 - if/elif/else
    - The if, elif, and else statements in Python control the flow of a program by executing code blocks based on conditions. if checks a condition; elif tests additional conditions if the first fails; else runs if no conditions are true. 
    For example, 
        age = 18
        if age>=18:

            print("Adult") #checks if age exceeds or equals 18.

        elif age<18 and age>=12:

            print("Teenage") #checks if age is less than 18 but above or equals 12.

        else:
        
            print("Child") #if none of the above statement is true