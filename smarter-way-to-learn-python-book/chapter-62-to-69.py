
#Bonus: Cryptography
#This is not setup properly
#In order to complete I must salt + password then hash the two
import os
from base64 import b64encode
class User():
    def __init__(self, email, password, hashy, salty):
        self.email = email
        self.password = password
        self.hashy = hashy
        self.salty = salty.b64encode(os.urandom(16)).decode()

    def login(self,password_attempt):
        if self.hashy == password_attempt:
            print("correct")
        else:
            print("incorrect")
    def dash_of_hash(self):
        return hash(self.password)
    def skosh_of_salt(self):
        salt = b64encode(os.urandom(16)).decode()
        salted_hash = str(hash(self.password))
        salty_pass = salted_hash + salt
        return salty_pass

employeeid308 = User("kamryn@pearson.com", "K@ty-P3rry143", "2870024076273424644")

print("My password is:", employeeid308.password,  "\nThe hash is:", employeeid308.dash_of_hash(), "\nThe salted hash is:", employeeid308.skosh_of_salt())

#Checks hash against one stored
#print(employeeid308.login("2870024076273424644"))


#Chapter 62
#w tells Python that you're opening a file to write to it
with open("whatever.txt", "w") as kams_file_handle:


#Chapter 63
with open("greet.txt", "w") as kams_file_handle:
    kams_file_handle.write("Hello, world!")
#or
greeting = "Hello, world!"
with open("greet.txt", "w") as kams_file_handle:
    kams_file_handle.write(greeting)


#Chapter 64
#r tells Python that you're opening a file to read it
with open("greet.txt", "r") as kams_file_handle:
    text_of_file = kams_file_handle.read()
print(text_of_file)
#or
#the default mode for an open statement is read so the r is not required
with open("greet.txt") as kams_file_handle:
    text_of_file = kams_file_handle.read()
print(text_of_file)


#Chapter 65
#a tells Python that you're opening a file to append to it
with open("greet.txt", "a") as f:
    f.write("\nHave a nice day!")


#Extra Chapters


#Chapter 66
from taxtool import calc_tax
tax_for_this_order = calc_tax(sales_total=1.00, tax_rate=.05)
print(tax_for_this_order)


#Chapter 67
import csv
with open("competitions.csv") as kams_file_handle:
    contents_of_file = csv.reader(kams_file_handle)


#Chapter 68
import csv
with open("competitions.csv") as kams_file_handle:
    contents_of_file = csv.reader(kams_file_handle)
    potter_competitions = []
    for each_line in contents_of_file:
        potter_competitions += each_line
print(potter_competitions)


#Chapter 69
target = input("Enter the name of a competition: ")
index_number_of_target = potter_competitions.index(target)
index_number_of_winner = index_number_of_target + 1
the_winner = potter_competitions[index_number_of_winner]
print("The winner was " + the_winner)


