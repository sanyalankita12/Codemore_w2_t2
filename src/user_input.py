def greeting():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    fav_language = input("What is your favourite language? ")
    difference=100-age
    year=difference+2026
    print(f"Hello,{name}! You're {age} years old. And your favourite programming language is {fav_language}.")
    print(f"You will turn 100 in year {year}")

greeting()

