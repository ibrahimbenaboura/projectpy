user = {
    "name": "ibrahim",
    "age": 19,
    "country": "algeria",
    "skills": ["python", "Excel"]
}

print(user)
print(user['country'])
print(user.get("country"))

print(user.keys())
print(user.values())

languages = {
    "one" : {
        "name" : "ibrahim",
        "lang" : "python"
    }
}

print(languages)
print(languages['one'])
print(languages['one']['lang'])
print(len(languages))
print(len(languages["one"]))

frameworkone = {
    "name" : "ibra",
    "progress" : "25%"
}
frameworktwo = {
    "name" : "lol",
    "progress" : "70%" 
}

allframework = {
    "one" : frameworkone,
    "two" : frameworktwo
}

print(allframework)

print(user)
user.clear()
print(user)

memeber = {
    "name" : "ibrahim"
}
print(memeber)
memeber["age"] = 19
print(memeber)
memeber.update({"country": "algeria"})
print(memeber)

b = memeber.copy()
print(b)
memeber.update({"skills": "python"})
print(memeber)
print(b)

print(memeber.keys())
print(memeber.values())

print(b)
print(b.setdefault("name", "lol"))
print(b)

print(b.setdefault("age", 20))
print(b)

print(b.setdefault("age"))
print(b)
b.update({"age": 20})
print(b.popitem)
print(b)

view = {
    "name" : "ibra",
    "skills": "python"
}

allitems = view.items()
print(view)
view["age"] = 20
print(allitems)

a = ('mk1', 'mk2', 'mk3')
c = "X"
print(dict.fromkeys(a, c))

name = " "
print(name.isspace())

print(bool("ibrahim"))
print(bool(""))
age = 19
country = "dz"
rank = 10

print(age > 18 and country == "dz")
print(age > 18 and country == "fr")

print(age > 18 or country == "dz")
print(age > 18 or country == "fr")

print(not age>18)



x = 10
y = 20

#x += y
#print(x)

#x *= y
#print(x)

#x /= y
#print(x)

#x **= y
#print(x)

#x %= y
#print(x)

x //= y
print(x)







