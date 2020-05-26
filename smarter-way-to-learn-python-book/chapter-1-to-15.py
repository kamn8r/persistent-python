#Chapter 6
#whats_left_over is equal to 1
#% modulo operator divides one number by another then gives you the remainder
#if numbers divide evenly modulo assigns 0 to the variable
whats_left_over = 10 % 3

age = age + 1
#is the same as
age += 1

#another example
age = 12
age += 50
#age is now equal to 72

#another example
age = 12
age -= 2
#age is now equal to 10

#another example
age = 12
amount_to_increment = 3
age += amount_to_increment
#age is now equal to 15


#Chapter 9
species = "cat"
if species == "cat":
    print("Yep, it's cat.")


#Chapter 11
species = "cat"
if species == "cat":
    print("Yep, it's cat.")
else:
    print("Nope, not cat.")

buy_score = 0
if donut_condition == "fresh":
    buy_score += 10
if donut_filling == "chocolate":
    buy_score += 5
if donut_price == "reasonable":
    buy_score += 7


#Chapter 12
if weight > 300 and time < 6:
    status = "try to recruit him"

if weight > 300 and time < 6 and age > 17 and height < 72:
    status = "try to recruit him"

if SAT > avg or GPA > 2.5 or parent == "alum":
    message = "Welcome to Leeds College!"

if (age > 65 or age < 21) and res == "US":


#Chapter 13
if c == d:
    if x == y:
        g = h
    elif a == b:
        g = h
    else:
        e = f
else:
    e = f


#Chapter 15
city_0 = "Atlanta"
city_1 = "Baltimore"
city_2 = "Chicago"
city_3 = "Denver"
city_4 = "Los Angeles"
city_5 = "Seattle"

cities = ["Atlanta", "Baltimore", "Chicago", "Denver", "Los Angeles", "Seattle"]

print("You are in " + cities[7])
