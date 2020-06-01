#Chapter 70
import csv
with open("whatever.csv", "w", newline="") as x:


#Chapter 71
import csv
with open("whatever.csv", "w", newline="") as x:
    data_handler = csv.writer(x, delimiter=",")


#Chapter 72
import csv
with open("whatever.csv", "w", newline="") as x:
    data_handler = csv.writer(x, delimiter=",")
    data_handler.writerow(["Year", "Event", "Winner"])
    data_handler.writerow(["1995", "Best-Kept Lawn", "None"])
    data_handler.writerow(["1999", "Gobstones", "Welch National"])


#Chapter 73
import csv
with open("whatever.csv", "a", newline="") as x:
    data_handler = csv.writer(x, delimiter=",")
    data_handler.writerow(["2006", "World Cup", "Burkina Faso"])
    data_handler.writerow(["2011", "Butter Cup", "France"])
    data_handler.writerow(["2012", "Coffee Cup", "Brazil"])


#Chapter 74
#with a list
import json
alphabet_letters = ["a","b","c"]
with open("alphabet_list.json","w") as f:
    json.dump(alphabet_letters, f)
#or
#with a dictionary
customer29876 = {
    "first name": "David",
    "last name": "Elliot",
    "address": "4803 Wellesley St.",
}
with open("customer_29876.json", "w") as f:
    json.dumps(customer29876, f)


#Chapter 75
import json
with open("customer_29876.json") as f:
    customer_29876 =json.load(f)
#print(customer_29876)
print(customer_29876["last name"])
