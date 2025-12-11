#print("hello world")
#fname = input('what\'s your first name')
#mname = input('what\'s your middle name')
#lname = input('what\'s your last name')

#fname = fname.strip().capitalize()
#mname = mname.strip().capitalize()
#lname = lname.strip().capitalize()

#print(f"Hello {fname} {mname} {lname} happy to see you")


#thename = input('what\'s your name ?').strip().capitalize()
#theeamil = input('what\'s your email ?').strip()

#theusername = theeamil[: theeamil.index("@")]
#thewebsite = theeamil[theeamil.index("@") +1 :]

#print(f"hello {thename} your email is {theeamil}")
#print(f"your user name is {theusername} \nand your website is {thewebsite}")

#age = int(input('what\'s your age ?'))

#print(type(age))

#months = age * 12
#days = months * 30
#hours = days * 24
#munites = hours * 60 
#secondes = munites * 60

#print('you lived for : ')
#print(f"{months} Months")
#print(f"{days} Days")
#print(f"{hours} Hours")
#print(f"{munites} Munites")
#print(f"{secondes} Secondes")

price= 100
isstudent = "no"
course = "python course"
country = input('what\'s your country ?')

if country == "algeria" : 
    if isstudent == "yes" : 
     print(f"hello because you\'re a student from {country}")
     print(f"the price of {course} will be {price - 80}")
    else :
     print(f"hello because you\'re from {country}")
     print(f"the price of {course} will be {price - 70}")
elif country == "maroc" : 
    if isstudent == "yes" : 
     print(f"hello because you\'re a student from {country}")
     print(f"the price of {course} will be {price - 60}")
    else : 
     print(f"hello because you\'re from {country}")
     print(f"the price of {course} will be {price - 50}")
else : 
    if isstudent == "yes" : 
     print(f"hello because you\'re from {country}")
     print(f"the price of {course} will be {price - 50}")
    else : 
     print(f"hello because you\'re a student from {country}")
     print(f"the price of {course} will be {price - 30}") 





