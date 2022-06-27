import pandas as pd
# Bring the pandas data analysis library into current environment.

fh = pd.read_csv("Billionaire.csv")
fh["NetWorth"] = fh["NetWorth"].str.replace("$", "", regex=True)
fh["NetWorth"] = fh["NetWorth"].str.replace("B", "", regex=True)
fh.NetWorth = fh.NetWorth.astype(float)
pd.set_option("display.max_columns", None)
# Read a csv file into data frame.
# Remove signs of "$" and "B" and then convert the NetWorth column to float


def search_by_name():
    name = input("Enter name: ")
    print(fh.loc[fh["Name"].str.contains(name)])
# Define a function that allows user to search a billionaire by entering his/her name


def search_by_rank():
    x = int(input("Enter rank from: "))
    y = int(input("to: "))
    if x <= y:
        print(fh.loc[(fh["Rank"] >= x) & (fh["Rank"] <= y)])
    else:
        print("Error: First input number must be smaller or equal to second input number")
        search_by_rank()
# Define a function that allows user to search billionaires within the range of the desired rankings
# Warn the user to enter logical ranking range


def search_by_networth():
    x = float(input("Enter networth (in billions) from: "))
    y = float(input("to: "))
    if x <= y:
        print(fh.loc[(fh["NetWorth"] >= x) & (fh["NetWorth"] <= y)])
    else:
        print("Error: First input number must be smaller or equal to second input number")
        search_by_networth()
# Define a function that allows user to search billionaires within the range of the desired net worth
# Warn the user to enter logical net worth range


def search_by_age():
    x = float(input("Enter age from: "))
    y = float(input("to: "))
    if x <= y:
        print(fh.loc[(fh["Age"] >= x) & (fh["Age"] <= y)])
    else:
        print("Error: First input number must be smaller or equal to second input number")
        search_by_age()
# Define a function that allows user to search billionaires within the range of the desired age
# Warn the user to enter logical age range


def search_by_country():
    country = input("Enter country: ")
    print(fh.loc[fh["Country"] == country])
# Define a function that allows user to search billionaires from the desired country


def search_by_source():
    source = input("Enter source/company: ")
    print(fh.loc[fh["Source"].str.contains(source)])
# Define a function that allows user to search billionaires from the desired company


def search_by_industry():
    industry = input("Enter industry: ")
    print(fh.loc[fh["Industry"].str.contains(industry)])
# Define a function that allows user to search billionaires from the desired industry


print("Which function would you like to search by?")
print("To search by name: type 1 \nTo search by rank: type 2 \nTo search by networth: type 3"
      "\nTo search by age: type 4 \nTo search by country: type 5 \nTo search by source/company: type 6 "
      "\nTo search by industry: type 7")
#Ask the user to choose which function he/she wants to use


def search_type():
    num = int(input("Type here: "))
    if num == 1:
        search_by_name()
    elif num == 2:
        search_by_rank()
    elif num == 3:
        search_by_networth()
    elif num == 4:
        search_by_age()
    elif num == 5:
        search_by_country()
    elif num == 6:
        search_by_source()
    elif num == 7:
        search_by_industry()
    else:
        print("You have entered an invalid number. Please enter number from 1 to 7")
        search_type()
# Define a function that corresponds to user's choice of function
# Warn the user to make a logical choice


search_type()






