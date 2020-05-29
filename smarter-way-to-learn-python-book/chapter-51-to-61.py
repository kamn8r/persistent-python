#Chapter 51
cleanest_cities = ["Cheyenne", "Santa Fe", "Tucson", "Great Falls", "Honolulu"]

user_input = ""
while user_input != "q":
    user_input = input("Enter a city name or type q to quit")
    if user_input != "q":
        for x in cleanest_cities:
            if user_input == x:
                print("It's one of the cleanest cities")
                break


#Chapter 52
best_katy_perry_songs = ["Dark Horse", "Roar", "Firework", "Small Talk", "Last Friday Night"]

keep_looping = True
while keep_looping == True:
    user_input = input("Enter your favorite Katy Perry song or type q to quit")
    if user_input != "q":
        for x in best_katy_perry_songs:
            if user_input == x:
                print("That is one of the best Katy Perry songs")
                break
    else:
        keep_looping = False


#Chapter 53
class Barbarian():


#Chapter 54
class Patient():
    def __init__(self, last_name):


#Chapter 55
class Patient():
    def __init__(self, last_name):
        self.last_name = last_name


#Chapter 56
class Patient():
    def __init__(self, last_name):
        self.last_name = last_name

pid4343 = Patient("Taleb")
pid4344 = Patient("Anand")
pid4345 = Patient("Oppenheimer")
pid4346 = Patient("Lin")
pid12902 = Patient("Nilsson")


#Chapter 57
class Patient():
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

pid4343 = Patient("Taleb", "Sue", 61)
pid4344 = Patient("Anand", "Punya", 29)
pid4345 = Patient("Oppenheimer", "Douglas", 15)
pid4346 = Patient("Lin", "Lilly", 48)
pid12902 = Patient("Nilsson", "Rhonda", 33)


#Chapter 58
age_of_patient = pid4343.age
print(age_of_patient)
#or
print(pid4343.age)


#Chapter 59
class Patient():
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
    def say_if_minor(self):
        if self.age < 21:
            print(self.first_name + " " + self.last_name + " is a minor")

pid4343 = Patient("Taleb", "Sue", 61)
pid4344 = Patient("Anand", "Punya", 29)
pid4345 = Patient("Oppenheimer", "Douglas", 15)
pid4346 = Patient("Lin", "Lilly", 48)
pid12902 = Patient("Nilsson", "Rhonda", 33)

pid4343.say_if_minor()


#Chapter 60
class Patient():
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
    def say_if_minor(self):
        if self.age < 21:
            print(self.first_name + " " + self.last_name + " is a minor")

pid4343 = Patient("Taleb", "Sue", 61)
pid4344 = Patient("Anand", "Punya", 29)
pid4345 = Patient("Oppenheimer", "Douglas", 15)
pid4346 = Patient("Lin", "Lilly", 48)
pid12902 = Patient("Nilsson", "Rhonda", 33)

pid4343.say_if_minor()


#Chapter 61
class Patient():
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
    #defining a method called say_if_minor inside of Patient class
    def say_if_minor(self):
        if self.age < 21:
            print(self.first_name + " " + self.last_name + " is a minor")
    #defining another method
    def change_last_name(self,new_last_name):
        self.last_name = new_last_name

pid4343 = Patient("Taleb", "Sue", 61)
pid4344 = Patient("Anand", "Punya", 29)
pid4345 = Patient("Oppenheimer", "Douglas", 15)
pid4346 = Patient("Lin", "Lilly", 48)
pid12902 = Patient("Nilsson", "Rhonda", 33)

pid4343.change_last_name("Ortega")
print(pid4343.last_name)

