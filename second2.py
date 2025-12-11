#MovieRate = 18
#age = 19
#if age < MovieRate :
#    print("this film is not good for you ")
#else :
#    print("this film is good for you ")




# print("#" * 80)
# print(" you can write the first letter or full name of the time unit".center(80, "#"))
# print("#" * 80)

# age = input("please write your age :").strip()
# unit = input("please choose time unit : Months, Weeks, Days").strip().lower()

# months = int(age) * 12
# weeks = months * 4
# days = int(months) * 365

# if unit == 'months' or unit == 'm' :
#     print("you choosed the unit Months.")
#     print(f"you lived for {months:,} Months.")
# elif unit == 'weeks' or unit == 'w' :
#     print("you choosed the unit Weeks.")
#     print(f"you lived for {weeks:,} Weeks.")
# elif unit == 'days' or unit == 'd' :
#     print("you choosed the unit Days.")
#     print(f"you lived for {days:,} Days.")

# countriesone = ["Egypt", "Ksa", "Kuwait", "Bahrain", "Syria"]
# countriesonediscount = 35

# countriestwo = ["France", "Algeria", "Spain", "Sweden", "Switzerland"]
# countriestwodiscount = 20

# MyCountry = "italy"

# if MyCountry in countriesone :
#     print(f"hello you have a discount equal to ${countriesonediscount}")
# elif MyCountry in countriestwo :
#     print(f"hello you have a discount equal to ${countriestwodiscount}")
# else :
#     print("you have no discount")

# Admins = ["Ibrahim", "Oussama", "Ahmed", "Mehdi", "Khaled"]

# name = input("please write your name :").strip().capitalize()

# if name in Admins :
#     print(f"hello {name} welcome back.")

#     option = input("delete or update your name ?").strip().capitalize()

#     if option == "Update" :
#         thenewname = input("your new name please :").strip().capitalize()
#         Admins[Admins.index(name)] = thenewname

#         print("name updated.")
#         print(Admins)
#     elif option == "Delete" :
#         Admins.remove(name)
#         print("name deleted.")
#         print(Admins)
# else :
#     statut = input("you are not an admin, add you Yes or No?").strip().capitalize()
#     if statut == "Yes" or statut == "Y" :
#         print("you have been added.")
#         Admins.append(name)
#         print(Admins)
#     elif statut == "No" or statut == "N" :
#         print("you are not added")

# a = 0
# while a < 15 :
#     print(a)
#     a += 1
# else :
#     print("loop is done")


# MyF = ["os", "ah", "kh", "mh", "mj", "bch"]

# a = 0

# while a < len(MyF) : # a < 6
#    print(f"#{str(a + 1).zfill(2)} {MyF[a]}")
#    a += 1
# else :
#    print("all friends printed to screen.")


# myfavouriteswebs = []
# maximumwebs = 5

# while maximumwebs > 0 :
#     web = input("website name without https:// ")
#     myfavouriteswebs.append(f"https://{web.strip().lower()}")
#     maximumwebs -= 1
#     print(f"your website is : {myfavouriteswebs}")
#     print(f"website added, {maximumwebs} places left")
# else :
#     print("bookmark is full, you can't add more")



# if len(myfavouriteswebs) > 0 :
#     myfavouriteswebs.sort()
#     index = 0
#     print("printing the list in your bookmark")
#     while index < len(myfavouriteswebs) :
#         print(myfavouriteswebs[index])
#         index += 1


# MyNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for number in MyNumbers :
#     if number %2 == 1 :
#         print(f"The Number {number} Is Odd.")
#     else : 
#         print(f"The Number {number} Is Even.")
# else : 
#     print("The Loop Is Finished.")


# MyName = "ibrahim"
# for letter in MyName : 
#     print(f" [ {letter.upper()} ]")


# myskills = {
#         "Css" : "10%" ,
#         "Python" : "20%" ,
#         "Html" : "30%"
# }
# # print(skills)

# for skill in myskills :
#     print(f"My Progress in Lan {skill} is : {myskills[skill]}")



# peoples = ["ibrahim", "lamine", "mohamed"]
# skills = ["python", "java", "css"]

# for person in peoples :
#     print(f" {person} :")
#     for skill in skills :
#         print(f"- {skill}")


# peoples = {
#     "ibrahim" : {
#         "python" : "30%" ,
#         "css" : "20%",   
#         "java" : "10%"     
#          },
#      "lamine" : {
#          "python" : "20%",
#          "css": "15%",
#          "java" : "25%"
#      }
# }

# # print(peoples)
# # print(peoples["ibrahim"]['python'])

# for name in peoples : 
#     print(f"Skills and progress for {name} is:")
#     for skill in peoples[name] :
#         print(f"{skill.upper()} => {peoples[name][skill]}")


# mynumbers = [1, 2, 3, 4, 5, 6]

# for number in mynumbers :
#     # print(number)
#     if number == 1 :
#         pass
#     print(number)



# mylang = {
#         'python' : '10%',
#         'css' : '20%',
#         'java' : '30%' 
# }


# for lang_key, lang_value in mylang.items() :

#    print(f"{lang_key.upper()} => {lang_value}")








# people = {
#     "ibrahim" : {
#         "python" : "5%",
#         "css" : "10%",
#         "java" : "15%"    
#         },
#     "lamine" : {
#          "python" : "20%",
#         "css" : "25%",
#         "java" : "30%"    
#     }    
# }

# for name, key in people.items() :
#     print(f"{name} your progres is :")
#     for child_key, child_value in key.items() :
#         print(f" {child_key} => {child_value}")


# def function_name() :
#     return "hello world"

# dataformfuntion = function_name()

# print(dataformfuntion)

# a, b, c = "ahmed", "ibrahim", "lamine"

# def say_hello(n):
#     print(f"hello {n}")
# say_hello(a)
# say_hello(b)
# say_hello(c)



# def calcul(n1, n2):
#    if type(n1) != int or type(n2) != int :
#     print("the value must be integer")
#    else :
#     print(n1 + n2)

# calcul(100, 200)


# def full_name(first, middle, last) :
#     print(f"hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")

# full_name("ibrahim", "ace", "benaboura")





# def say_hello(*peoples) :
#      for name in peoples :
#         print(f"hello {name}")

# say_hello("ibrahim", "benaboura", "ace")


# def skills_ik(name, *skills) :
#     print(f"hello {name} your skills is :")
#     for skill in skills :
#         print(f"- {skill}")
# skills_ik("ibrahim", "python", "R", "SQL", "C++")



# def say_hello(name = "Unknown", age = "Unknown", country = "Unknown"):
#     print(f"hello {name} your age is {age} your country is {country}")

# say_hello("ibrahim ","20", "dz" )


# myskills = {
#     "html" : "20%",
#     "css" : "30%",
#     "py" : "40%",
#     "java" : "50%"
# }

# def show_skills(**skills) :
#     for skill, value in myskills.items() :
#         print(f"- {skill} => {value}")

# show_skills(**myskills)

# mytuple = ["html", "css", "py"]

# myskills = {
#     'html' : "20%",
#     'css' : "30%",
#     'py' : "40%"
# }

# def show_skills(name, *skills, **skillswithprogress) :
#     print(f"hello {name} \nskills without progress is : ")

#     for skill in skills :
#         print(f"- {skill}")
    
#     print("skill with progress is :")
#     for skill_key, skill_value in skillswithprogress.items() :
#         print(f"- {skill_key} => {skill_value}")

# show_skills("ibrahim", *mytuple, **myskills)







# mytuple = ["html", "css", "py"]

# myskills = {
#     'html' : "20%",
#     'css' : "30%",
#     'py' : "40%"
# }

# def show_skills(name, *mytuple, **myskills) :
#     print(f"hello {name} \nskills without progress is : ")

#     for skill in mytuple :
#         print(f"- {skill}")
    
#     print("skill with progress is :")
#     for skill_key, skill_value in myskills.items() :
#         print(f"- {skill_key} => {skill_value}")

# show_skills("ibrahim", *mytuple, **myskills)


#global and local scoope 


# x = 4
# def one() :
#     global x
#     x = 3
#     print(x)

# def two() :

#     print(x)
    

# print(x)
# one()
# print(x)
# two()


# def cleanword(word) :
#     if len(word) == 1 :
#         return word
#     if word[0] == word[1] :
#         return cleanword(word[1:])
#     return word[0] + cleanword(word[1:])

# print(cleanword("ppppyyyytttthhhooonnn"))





# def sayhello(name) : return f"hello {name}"

# hello = lambda name : f"Hello {name}"

# print(sayhello("ibrahim"))
# print(hello("mehdi"))

# print(sayhello.__name__)
# print(hello.__name__)

# print(type(hello))


# import os

# os.chdir(r"C:\Users\A\Desktop")


# file = open(r"C:\Users\A\Desktop\projectpy\test.txt")


# print(file)
# print(file.name)

# print(file.mode)
# print(file.encoding)


# print(file.read())

# print(file.read(5))


# print(file.readline(2))



# for line in file :
#     print(line)
#     if line.startswith("06") :
#        break



# file.close()



# file = open(r"C:\Users\A\Desktop\projectpy\test.txt", "w")

# import os

# os.remove(r"C:\Users\A\Desktop\projectpy\test.txt")


# x = [0, []]

# # if all(x) :
# #     print("all elements is true")
# # else :
# #     print("at least one element is false")


# if any(x) :
#     print("there is at least one element is true")
# else :
#     print("all elements is false")



# print(bin(1))


# a = 1
# b = 2


# print(id(a))
# print(id(b))





# a =[1, 5, -6, 100]

# print(sum(a))
# print(sum(a, 10))


# print(round(166.5117, 3))

# print(list(range(0, 10, 2)))




# print("hello", "world", "i", "love", "Python", sep="|")

# print("first line", end= "\n")
# print("second line", end="\\")
# print("third line")




# print(abs(-100))

# print(pow(2, 5, 10))
# print(min(1, 2, 3))
# print(max(1, 2, 3))

# A = ["A", "B", "C", "D", "E", "F"]

# print(A[slice(2, 5)])






# def checknumber(num) :
#     if num > 10 :
#         return num
    

# mynumbers = [1, 16, 10, 100, 4]

# myresults = filter(checknumber, mynumbers)

# for number in myresults :
#     print(number)





# def checkname (name) :
#     return name.startswith("O")

# mynames = ["Ibrahim", "Osama", "Khaled", "Othman"]

# myresults = filter(checkname, mynames)

# for person in myresults :
#     print(person)




# mynames = ["issa", "ibrahim", "ayoub"]


# for person in filter(lambda name : name.startswith("i"), mynames) :
#     print(person)
# from functools import reduce

# mynumbers = [5, 55, 100, 10]


# myresult = reduce(lambda num1, num2 : num1 + num2, mynumbers)

# print(myresult)






# MySkills = ["Html", "Css", "Js", "Python"]

# myskillscounter = enumerate(MySkills, 0)

# for counter, skill in myskillscounter :
#     print(f"-{counter} : {skill}")




# print(help(print))




# myname = "ibrahim"
# print(reversed(myname))

# for letter in myname :
#     print(letter)

# import random 
# print(random)
# print(f"print Random Float Number {random.random()}")



# print(dir(random))

# from random import randint, random

# print(f"Print random float {random()}")
# print(f"print random integer {randint(100, 900)}")



# import ace as ee 

# ee.sayhello("ibrahim")

# ee.sayhowareyou("ibrahim")



# from ace import sayhello as ss 
# ss("ibrahim")


# import pyfiglet
# import termcolor


# # print(pyfiglet.figlet_format("Ace"))
# # print(termcolor.colored("Ace", color ="red"))


# print(termcolor.colored(pyfiglet.figlet_format("Ace"), color ="red"))




# import datetime

# # print(datetime.datetime.now())
# # print(datetime.datetime.now().month)
# # print(datetime.datetime.now().day)
# # print(datetime.datetime.now().year)


# MyBirthday = datetime.datetime(2006, 4, 21)

# # Today = datetime.datetime.now()

# # print(f"i lived for {(Today - MyBirthday).days} Days.")


# print(MyBirthday.strftime("%a"))
# print(MyBirthday.strftime("%A"))
# print(MyBirthday.strftime("%b"))
# print(MyBirthday.strftime("%B"))

# print(MyBirthday.strftime("%A %d %B %Y"))




# def MyGenerator() :
#     yield 1
#     yield 2
#     yield 3
#     yield 4

# MyGen = MyGenerator()



# # for number in MyGen :
# #     print(number)

# print("before")
# print(next(MyGen))
# print("after")
# print(next(MyGen))

# for number in MyGen :
#     print(number)



# def MyDecorator(func) :
#     def nestedfunc(num1, num2) :
#         if num1 < 0 or num2 < 0 :
#             print("Beware one of the numbers is less than zero")
#         func(num1, num2)
#     return nestedfunc 


# def Mydecorator2(func) :
#     def nestedfunc(num1, num2) :
#         if num2 == 10 :
#              print("the second number is equal to ten")
#         func(num1, num2)
#     return nestedfunc  

# @MyDecorator
# @Mydecorator2
# def calculate(n1, n2) :
#     print(n1 + n2)
# calculate(-4, 10)




































































