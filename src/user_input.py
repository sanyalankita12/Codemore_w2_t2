from datetime import datetime

#---Creating a function for greeting and calculating the year user will turn 100---
def greeting():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    fav_language = input("What is your favourite programming language? ")
    difference=100-age
    current_year = datetime.now().year
    year = current_year + (100 - age)
    print(f"Hello,{name}! You're {age} years old. And your favourite programming language is {fav_language}.")
    print(f"You will turn 100 in year {year}")

greeting()

