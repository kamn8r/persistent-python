
#Chapter 16
cities.append("New York")

cities = cities + ["Dubuque", "New Orleans"]

cities.insert(2,"Souix City")

#how to rename item in list
cities[2] = "Houston"

print(cities)

second_longer_cities_list = cities + ["Des Moines", "Santa Fe"]
print(second_longer_cities_list)

todays_tasks = []

todays_tasks = todays_tasks + ["Walk dog","buy groceries"]
#or
todays_tasks += ["sweep"]

print(todays_tasks)


#Chapter 17
#copying elements 2-4 from other list
smaller_list_of_cities = cities[2:5]
#or
#if you are copying from the beginning of the list, you can omit 0
smaller_list_of_cities = cities[:5]
#if the last element of the slice is the last element you can omit second number
smaller_list_of_cities = cities[2:]


#Chapter 18
tasks = ["email Frank", "call Sarah", "meet with Zach"]

del tasks[0]
#or
tasks.remove("call Sarah")


#Chapter 19
tasks = ["email Frank", "call Sarah", "meet with Zach"]

#takes item from tasks list and assigns it to variable
latest_task_accomplished = tasks.pop(1)

#append one list to another
tasks_accomplished = []
tasks_accomplished.append(latest_task_accomplished)

#pop item from a list and add it to another
tasks_accomplished.append(tasks.pop(1))

#insert item from list to specific spot after removing from another list
#aka it strikes second element of tasks list and inserts as second in tasks_accomplished
tasks_accomplished.insert(1,tasks.pop(1))

#to pop last element in a list don't specify a number
latest_task_accomplished = tasks.pop()

#pops the first element of y list and appends it to end of list x
x.append(y.pop(0))


#Chapter 20
#Tuples
#Tuples use ( ) instead of lists which use [ ]
states_in_order_of_founding = ("Delaware", "Pennsylvania", "New Jersey", "Georgia")

second_state_founded = states_in_order_of_founding[1]

print("The seconds state was " + second_state_founded)


#Chapter 21
cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson", "Great Falls", "Honolulu"]

city_to_check="Great Falls"

#there are 3 variables in this for loop
#they are: a_clean_city, city_to_check, and cleanest_cities
#a_clean_city stores a list element each time through the loop
for a_clean_city in cleanest_cities:
    if a_clean_city == city_to_check:
        print("It's one of the cleanest cities")
        break

#or
z= "Great Falls"
for x in y:
    if x == z:
        print("It's one of the cleanest cities")
        break

#or
#for each element, one at a time, in the list:
    #do something with that element
        #do something if line 2 is met


#Chapter 22
first_names = ["BlueRay", "Upchuck", "Lojack", "Gizmo", "Do-Rag"]
last_names = ["Zzz", "Burp", "Dogbone", "Droop"]
full_names= []

for a_first_name in first_names:
    for a_last_name in last_names:
        full_names.append(a_first_name + " " + a_last_name)

print(full_names)


#Chapter 23
cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson", "Great Falls", "Honolulu"]

city_to_check = input("Enter the name of a city: ")

monthly_income = input("Enter your monthly income :")


#Chapter 24
cleanest_cities = ["cheyenne", "santa fe", "tucson", "great falls", "honolulu"]
city_to_check = input("Enter your city: ")
city_to_check = city_to_check.lower()
for a_clean_city in cleanest_cities:
    if city_to_check == a_clean_city:
        print(city_to_check.title() + " is one of the cleanest cities.")


#Chapter 25
jobs_to_do_list = ["email", "texting", "calls"]
customer_29876 = {"first name": "David", "last name": "Elliot", "address": "4803 Wellesley St."}

#this now contains the string 4803 Wellesley St.
address_of_customer = customer_29876["address"]

print(address_of_customer)


#Chapter 28
rankings = {5:"Finland", 2:"Norway", 3:"Sweden", 7:"Iceland"}
second_ranking_country = rankings[2]

print(second_ranking_country)

