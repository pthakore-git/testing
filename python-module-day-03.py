#!/usr/bin/env python
# coding: utf-8

# # 3.3 A Deeper Dive Into Python - 🐍

# # Activity 01 - Student Turn - Cereal Cleaner - 👩‍🎓👨‍🎓 
# 
# In this activity, you will create an application that reads in cereal data from a CSV file and then prints only those cereals that contain 5 or more grams of fiber.
# 
# ## Instructions
# 
# * Read the file using the code in the notebook, `cereal.csv` and start by skipping the header row. See hints below for this.
# 
# * Read through the remaining rows and find the cereals that contain five grams of fiber or more, printing the data from those rows to the terminal.
# 
# ## Hints
# 
# * Every value within the csv is stored as a string, and certain values have a decimal. This means that they will have to be cast to be used.
# 
# * `csv.reader` begins reading the CSV file from the first row. `next(csv_reader, None)` will skip the header row.
# 
#   * Refer to this Stack Overflow post on [how to skip the header](https://stackoverflow.com/a/14257599) for more information.
# 
# * Integers in Python are whole numbers and, as such, cannot contain decimals. Decimal numbers As such, your numbers containing decimal points will have to be cast as a `float`.
# 
# ## Bonus
# 
# Try the activity again, but this time use `cereal_bonus.csv`, which does not include a header.
# 
# ## References
# 
# Crawford, C. (2017, October 24). 80 cereals. [https://www.kaggle.com/crawford/80-cereals](https://www.kaggle.com/crawford/80-cereals), originally sourced from [http://lib.stat.cmu.edu/datasets/1993.expo/](http://lib.stat.cmu.edu/datasets/1993.expo/)
# 
# ---

# In[ ]:


import os
import csv

cereal_path = os.path.join(".", "Resources", "cereal.csv")

# Open and read csv
with open(cereal_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csvreader:

        # Convert row to float and compare to grams of fiber
        if(float(row[7])>=5):
            print(row)


# In[ ]:


# Bonus 

import os
import csv

cereal_csv = os.path.join(".", "Resources", "cereal_bonus.csv")

with open(cereal_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # @NOTE: This time, we do not use `next(csv_reader)` because there is no header for this file

    # Read through each row of data after the header
    for row in csvreader:

        # Convert row to float and compare to grams of fiber
        if(float(row[7])>=5):
            print(row)


# <details>
#   <summary><strong>✅ Solution 01 Click HERE</strong></summary>
# 
# ```python
# import os
# import csv
# 
# cereal_csv = os.path.join(".", "Resources", "cereal.csv")
# 
# # Open and read csv
# with open(cereal_csv) as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
# 
#     # Read the header row first (skip this part if there is no header)
#     csv_header = next(csv_file)
#     print(f"Header: {csv_header}")
# 
#     # Read through each row of data after the header
#     for row in csv_reader:
# 
#         # Convert row to float and compare to grams of fiber
#         if float(row[7]) >= 5:
#             print(row)          
# ```
# 
# 
# </details>
# 
# 

# 
# <details>
#   <summary><strong>✅ Solution 01 Bonus Click HERE</strong></summary>
# 
# ```python
# import os
# import csv
# 
# cereal_csv = os.path.join(".", "Resources", "cereal_bonus.csv")
# 
# with open(cereal_csv) as csvfile:
#     csv_reader = csv.reader(csvfile, delimiter=",")
# 
#     # @NOTE: This time, we do not use `next(csv_reader)` because there is no header for this file
# 
#     # Read through each row of data after the header
#     for row in csv_reader:
# 
#         # Convert row to float and compare to grams of fiber
#         if float(row[7]) >= 5:
#             print(row)
# ```
#     
# </details>
# 

# # Activity 02 - Instructor Turn - Dictionary - 👩‍🏫🧑‍🏫

# In[ ]:


# Unlike lists, dictionaries store information in pairs
# ---------------------------------------------------------------

# Create a dictionary to hold the actor's names.
actors = {}

# Create a dictionary using the built-in function.
actors = dict()

# A dictionary of an actor.
actors = {"name": "Tom Cruise"}
print(f'{actors["name"]}')

# Add an actor to the dictionary with the key "name"
# and the value "Denzel Washington".
actors["name"] = "Denzel Washington"

# Print the actors dictionary.
print(actors)

# Print only the actor.
print(f'{actors["name"]}')


# In[ ]:


# A list of actors
actors_list = [
    "Tom Cruise",
    "Angelina Jolie",
    "Kristen Stewart",
    "Denzel Washington"]

# Overwrite the value, "Denzel Washington", with the list of actors.
actors["name"] = actors_list

# Print the first actor
print(f'{actors["name"][0]}')

# ---------------------------------------------------------------


# In[ ]:


# A dictionary can contain multiple pairs of information
actress = {
    "name": "Angelina Jolie",
    "genre": "Action",
    "nationality": "United States"
}

# ---------------------------------------------------------------


# In[ ]:


# A dictionary can contain multiple types of information
another_actor = {
    "name": "Sylvester Stallone",
    "age": 62,
    "married": True,
    "best movies": [
        "Rocky",
        "Rocky 2",
        "Rocky 3"]}
print(f'{another_actor["name"]} was in {another_actor["best movies"][0]}')
# ---------------------------------------------------------------


# In[ ]:


# A dictionary can even contain another dictionary
film = {
    "title": "Interstellar",
    "revenues": {
        "United States": 360,
        "China": 250,
        "United Kingdom": 73
    }
}
print(f'{film["title"]} made {film["revenues"]["United States"]}'" million dollars in the US.")
# ---------------------------------------------------------------


# # Activity 03 - Student Turn - Hobby Book: Dictionaries - 👩‍🎓👨‍🎓 
# 
# In this activity, you will create and access dictionaries that are based on your own hobbies.
# 
# ## Instructions
# 
# 1. Create a dictionary to store the following information:
# 
# * Your name
# * Your age
# * A list of a few of your hobbies
# * A dictionary that includes a few days and the time you typically wake up on those days
# 
# 2. Print out your name, how many hobbies you have, and a time you typically wake up during the week.
# 
# - - -

# In[ ]:


# Dictionary full of info
me  = {"name": "Paulin",
       "age": 47,
       "hobbies": ["dancing","foodie"],
       "wake_up_time":{
           "Saturday": 11, "Sunday": 11
           }
        }

# Print out results are stored in the dictionary
print(f"My name is {me['name']} & I have {len(me['hobbies'])} hobbies.")
print(f"I am {me['age']} years old.")
print(f"I wake up on Sunday at {me['wake_up_time']['Sunday']} AM")


# In[ ]:





# In[ ]:





# In[ ]:





# <details>
#   <summary><strong>✅ Solution 03 Click HERE</strong></summary>
# 
# ```python
# # Dictionary full of info
# my_info = {"name": "Rex",
#            "occupation": "dog",
#            "age": 21,
#            "hobbies": ["barking", "eating", "sleeping", "loving my owner"],
#            "wake-up": {"Mon": 5, "Friday": 5, "Saturday": 10, "Sunday": 9}}
# 
# # Print out results are stored in the dictionary
# print(f'Hello I am {my_info["name"]} and I am a {my_info["occupation"]}')
# print(f'I have {len(my_info["hobbies"])} hobbies!')
# print(f'On the weekend I get up at {my_info["wake-up"]["Saturday"]}')
# ```
# 
# </details>

# # Activity 04 - Everyone Turn - List Comprehensions - 👩‍🏫🧑‍🏫 👩‍🎓👨‍🎓
# 
# 
# 

# In[ ]:


fish = "halibut"

# Loop through each letter in the string
# and push to an array
letters = []
for letter in fish:
    letters.append(letter)

print(letters)


# In[ ]:


# List comprehensions provide concise syntax for creating lists
letters = [letter for letter in fish]

print(letters)



# In[ ]:


# We can manipulate each element as we go
capital_letters = []
for letter in fish:
    capital_letters.append(letter.upper())

print(capital_letters)



# In[ ]:


# List Comprehension for the above
capital_letters = [letter.upper() for letter in fish]

print(capital_letters)



# In[ ]:


# We can also add conditional logic (if statements) to a list comprehension
july_temperatures = [87, 85, 92, 79, 106]
hot_days = []
for temperature in july_temperatures:
    if temperature > 90:
        hot_days.append(temperature)
print(hot_days)



# In[ ]:


# List Comprehension with conditional
hot_days = [temperature for temperature in july_temperatures if temperature > 90]

print(hot_days)


# # Activity 05 - Student Turn - List Comprehensions - 👩‍🎓👨‍🎓
# 
# In this activity, you’ll use list comprehensions to compose a wedding invitation, which you will send to every name on your mailing list.
# 
# ## Instructions
# 
# * Fill the cell below.
# 
# * Run the provided program. Note that nothing forces you to write the name properly in title case&mdash;for example, as "Jane" instead of "jAnE". You will use list comprehensions to fix this.
# 
#   * First, use list comprehensions to create a new list that contains the lowercase version of each of the names your user provided.
# 
#   * Then, use list comprehensions to create a new list that contains the title-case versions of each of the names in your lowercase list.
# 
# ## Hint
# 
# * Check out the documentation for the [title method](https://docs.python.org/3/library/stdtypes.html#str.title).
# 
# - - -

# In[ ]:


# TODO 
names = []
for _ in range(5):
    name = input("Please enter the name of someone you know. ")
    names.append(name)

# @TODO: Use a list comprehension to create a list of lowercased names
lowercased = [name.lower() for name in names]

# @TODO: Use a list comprehension to create a list of title cased names
# https://www.tutorialspoint.com/python/string_title.htm
titlecased = [name.title() for name in lowercased]

invitations = [
    f"Dear {name}, please come to the wedding this Saturday!" for name in titlecased]

for invitation in invitations:
    print(invitation)


# In[ ]:





# In[ ]:





# <details>
#   <summary><strong>✅ Solution 05 Click HERE</strong></summary>
# 
# ```python
# names = []
# for _ in range(5):
#     name = input("Please enter the name of someone you know. ")
#     names.append(name)
# 
# lowercased = [name.lower() for name in names]
# title cased = [name.title() for name in lowercased]
# invitations = [
#     f"Dear {name}, please come to the wedding this Saturday!" for name in title cased]
# 
# for invitation in invitations:
#     print(invitation)
# ```
#     
#     
# </details>

# # Activity 06 - Everyone Turn - Functions - 👩‍🏫🧑‍🏫 👩‍🎓👨‍🎓

# In[ ]:


# Basic Definition
def name(parameters):
    # code goes here
    return


# Simple Function with no parameters
def show():
    print(f"Hi!")


# you use parentheses to run the code in a function
show()




# In[ ]:


# Simple function with one parameter
def show(message):
    print(message)


# Think of the parameter `message` as a variable
# You assign the string "Hello, World!" when you call the function
# This is like saying `message = "Hello, World!"`
show("Hello, World!")




# In[ ]:


# Functions can have more than one parameter
def make_quesadilla(protein, topping):
    quesadilla = f"Here is a {protein} quesadilla with {topping}"
    print(quesadilla)


# Supply the arguments (values) when calling the function
make_quesadilla("beef", "guacamole")
make_quesadilla("chicken", "salsa")



# In[ ]:


# @NOTE: Order is important when supplying arguments!
make_quesadilla("sour cream", "beef")


# We can also specify default values for parameters
def make_quesadilla(protein, topping="sour cream"):
    quesadilla = f"Here is a {protein} quesadilla with {topping}"
    print(quesadilla)


# Make a quesadilla using the default topping
make_quesadilla("chicken")

# Make a quesadilla with a new topping
make_quesadilla("beef", "guacamole")




# In[ ]:


# Functions can return a value
def square(number):
    return number * number


# You can save the value that is returned
squared = square(2)
print(squared)

# You can also just print the return value of a function
print(square(2))
print(square(3))


# # Activity 07 - Student Turn - Functions - 👩‍🎓👨‍🎓
# 
# In this activity, you will write a function to compute the arithmetic mean (average) for a list of numbers.
# 
# ## Instructions
# 
# * Write a function called `average` that accepts a list of numbers.
# 
#   * The function `average` should return the arithmetic [mean](https://en.wikipedia.org/wiki/Arithmetic_mean) (average) for a list of numbers.
# 
# * Test your function by calling it with different values and printing the results.
# 
# - - -
# 

# In[ ]:


# @TODO: Write a function that returns the arithmetic average for a list of numbers
def average(numList):
    sum = 0
    for i in numList:
        sum = sum + i
        
    return sum/len(numList)


# In[ ]:


# Test your function with the following:

print(average([1, 5, 9]))
# print(average(range(11)))


# In[ ]:





# <details>
#   <summary><strong>✅ Solution 07 Click HERE</strong></summary>
# 
# ```python
# # Write a function that returns the arithmetic average for a list of numbers
# def average(numbers):
#     length = len(numbers)
#     total = 0.0
#     for number in numbers:
#         total += number
#     return total / length
# 
# 
# # Test your function with the following:
# print(average([1, 5, 9]))
# print(average(range(11)))
# 
# 
# ```
# </details>

# # Activity 08 - Student Turn - Graduation - 👩‍🎓👨‍🎓
# 

# # Graduating Functions
# 
# In this activity, you will create a function that searches a list of students and graduates by state to determine state graduation rates for public, private nonprofit, and private for-profit institutions.
# 
# ## Instructions
# 
# * Analyze the code and CSV provided, looking specifically for what needs to still be added to the application.
# 
# * Using the starter code provided, create a function called `print_percentages` which takes in a parameter called `state_data` and does the following:
# 
#   * Uses the data stored within `state_data` to calculate the estimated graduation rates in each category of Title IV 4-year institutions (public, non-profit private, and for-profit private).
# 
#   * Prints out the graduation rates for each school type for the state to the terminal.
# 
# Note: Some states do not have non-profit or for-profit private schools, so data must be checked for zeros
# 
# ## Bonus
# 
# * Still within the `print_percentages()` function, calculate the overall graduation rate, and create a conditional that checks a state's overall graduation rate and prints either "Graduation success" to the screen if the number was greater than fifty or "State needs improvement" if the number was less than 50.
# 
# ## References
# 
# Data Source: U.S. Department of Education, National Center for Education Statistics, IPEDS, Winter 2012-13, Graduation Rates component (final data). [https://nces.ed.gov/datalab/table/library/detail/12572](https://nces.ed.gov/datalab/table/library/detail/12572)
# 
# - - -

# In[30]:


import os
import csv

# Path to collect data from the Resources folder
graduation_csv = os.path.join('.', 'Resources', 'graduation_data.csv')


# Define the function and have it accept the 'state_data' as its sole parameter
def print_percentages(state_data):
    print(state_data)
    state = str(state_data[0])
    public_students = int(state_data[1])
    public_grads = int(state_data[2])
    nonProfitPrivate_students = int(state_data[3])
    nonProfitPrivate_grads = int(state_data[4])
    forProfitPrivate_students = int(state_data[5])
    forProfitPrivate_grads = int(state_data[6])
    
# Find the total students
    total_students = public_students + nonProfitPrivate_students +  forProfitPrivate_students

# Find the total graduates
    total_grads = public_grads + nonProfitPrivate_grads + forProfitPrivate_grads
     

# Find the public school graduation rate
    public_grad_rate = (public_grads/public_students)*100
    

# Remember that some states do not have nonprofit or forprofit private schools
# Find the non-profit school graduation rate
    if(nonProfitPrivate_students == 0):
        nonProfitRate = 0
    else:
        nonProfitRate = (nonProfitPrivate_grads/nonProfitPrivate_students)*100

# Find the for-profit school graduation rate
    if(forProfitPrivate_students == 0):
        forProfitRate = 0
    else:
        forProfitRate = (forProfitPrivate_grads/forProfitPrivate_students)*100

# Calculate the overall graduation rate
    overallGradRate = (total_grads/total_students)*100
    
# Print out the state's name and its graduation rates
    if(overallGradRate > 50):
        message = ("Graduation success!")
    else:
        message = ("State needs improvement.")    
     
    print(f"Stats for {state}:") 
    print(f"Public School Grad Rate: {public_grad_rate}")
    print(f"Non Profit Private School Grad Rate: {nonProfitRate}")
    print(f"For Profit Private School Grad Rate: {forProfitRate}")
    print(f"Overall grad rate: {overallGradRate}")
    print(f"{message}")      
          
# Read in the CSV file
with open(graduation_csv, 'r') as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Prompt the user for what state they would like to search for
    state_to_check = input("What state do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the state's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if state_to_check == row[0]:
            print_percentages(row)


# In[ ]:





# <details>
#   <summary><strong>✅ Solution 08 Click HERE</strong></summary>
# 
# ```python
# import os
# import csv
# 
# # Path to collect data from the Resources folder
# graduation_csv = os.path.join('.', 'Resources', 'graduation_data.csv')
# 
# 
# # Define the function and have it accept the 'state_data' as its sole parameter
# def print_percentages(state_data):
#     # For readability, it can help to assign your values to variables with descriptive names
#     # CSV headers: State or jurisdiction, Adjusted cohort (Public), Completers (Public),
#     # Adjusted cohort (Nonprofit Private), Completers (Nonprofit Private), 
#     # Adjusted cohort (For-profit Private), Completers (For-profit Private)
#     state = str(state_data[0])
#     public_students = int(state_data[1])
#     public_graduates = int(state_data[2])
#     nonprofit_students = int(state_data[3])
#     nonprofit_graduates = int(state_data[4])
#     forprofit_students = int(state_data[5])
#     forprofit_graduates = int(state_data[6])
# 
#     # Total students can be found by adding students of each category together
#     total_students = public_students + nonprofit_students + forprofit_students
#     # Total graduates can be found by adding graduates of each category together
#     total_graduates = public_graduates + nonprofit_graduates + forprofit_graduates
# 
#     # Public grad rate can be found by dividing the total public graduates by the total public 
#     # students and multiplying by 100
#     public_grad_rate = (public_graduates / public_students) * 100
# 
#     # Note that some states do not have nonprofit or forprofit private schools, so data must be checked 
#     # for zeros
# 
#     # Nonprofit grad rate can be found by dividing the total nonprofit graduates by the total nonprofit 
#     # students and multiplying by 100
#     if nonprofit_students == 0:
#         nonprofit_grad_rate = 0
#     else:
#         nonprofit_grad_rate = (nonprofit_graduates / nonprofit_students) * 100
# 
#     # Forprofit grad rate can be found by dividing the total forprofit graduates by the total forprofit 
#     # students and multiplying by 100
#     if forprofit_students == 0:
#         forprofit_grad_rate = 0
#     else:
#         forprofit_grad_rate = (forprofit_graduates / forprofit_students) * 100
# 
#     # Calculate the overall graduation rate
#     overall_grad_rate = (total_graduates / total_students) * 100
# 
#     # If the overall graduation rate is over 50, message is "Graduation success". 
#     # Otherwise it is "State needs improvement".
#     if overall_grad_rate > 50:
#         message = "Graduation success"
#     else:
#         message = "State needs improvement"
# 
#     # Print out the state's name and their graduation rates
#     print(f"Stats for {state}")
#     print(f"Public School Graduation Rate: {str(public_grad_rate)}")
#     print(f"Private Non-Profit School Graduation Rate: {str(nonprofit_grad_rate)}")
#     print(f"Private For-Profit School Graduation Rate: {str(forprofit_grad_rate)}")
#     print(f"Overall Graduation Rate: {str(overall_grad_rate)}")
#     print(f"{message}")
# 
# 
# # Read in the CSV file
# with open(graduation_csv, 'r') as csvfile:
# 
#     # Split the data on commas
#     csvreader = csv.reader(csvfile, delimiter=',')
# 
#     header = next(csvreader)
# 
#     # Prompt the user for what state they would like to search for
#     state_to_check = input("What state do you want to look for? ")
# 
#     # Loop through the data
#     for row in csvreader:
# 
#         # If the state's name in a row is equal to that which the user input, run the 'print_percentages()' function
#         if state_to_check == row[0]:
#             print_percentages(row)
# ```
# </details>

# # Activity 09 - Everyone - Adding More to the Repo - 👩‍🎓👨‍🎓👩‍🏫🧑‍🏫
# 
# 
# * You only added files using the GitHub website, which works well enough when just dealing with one or two files. What happens when we need to quickly add multiple files?
# 
#   * The command line comes to the rescue!
# 
# * Creating a repo and adding files with Terminal/Git Bash.
# 
#   * First, create a new repo.
# 
#   * From the repo page, click the green box in the top-right labeled "Clone or download", select "Use SSH", and copy the link to the clipboard, as captured in the following GIF:
# 
#   ![clone repo](./images/GitClone.gif)
# 
#   * Open Terminal (or Git Bash for Windows users), and navigate to the home folder using `cd ~`.
# 
#   * Type `git clone <repository link>` in the terminal to clone the repo to the current directory. Once this code has run, everyone should find a folder with the same name as the repo, as captured in the following image:
# 
#     ![terminal clone](./images/GitClone_command.png)
# 
#   * Open the folder in VS Code, and create two python script files, named `script01.py` and `script02.py`.
# 
#   * Then, open Terminal/Git Bash, and navigate to the repo folder. Run the following lines, explaining each line as you go.
# 
#   ```bash
#   # Displays that status of files in the folder
#   git status
# 
#   # Adds all the files into a staging area
#   git add .
# 
#   # Check that the files were added correctly
#   git status
# 
#   # Commits all the files to your repo and adds a message
#   git commit -m <add commit message here>
# 
#   # Pushes the changes up to GitHub
#   git push origin main
#   ```
# 
#   * Finally, navigate to the repo on [Github.com](https://github.com/) to confirm that the changes have been pushed up.
# 
# * Make sure every student was able to successfully clone a repo, add files to the repo, commit the changes, and then push the changes to GitHub, all from the command line.
# 
# 
# 
# 
# In this activity, you will create a new repository, clone it, and add files via command line
# 
# ## Instructions
# 
# * Using the repo that we just created, make or add the following changes:
# 
# 
# * Add new lines of code to one of the Python files.
# * Create a new folder.
# * Add a file to the newly created folder.
# * Add, commit, and push the changes.
# * Delete the new folder.
# * Add, commit, and push the changes again.
# 

# In[ ]:




