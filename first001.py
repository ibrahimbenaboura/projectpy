from pickle import APPEND


print(type(100.9)) # float
print(type(100)) # int
print(type("hello pyhton")) #string
print(type((1, 2, 3, 4))) #tuple
print(type([1, 2, 3, 4, 5])) #list
print({"one": 1, "two": 2, "three": 3}) #dictionery
print(type(2==2)) #boolean
Name = "ibrahim"
print(Name)
print("hello\bworld")# remove o
print("hello\nworld")#new line
print("hello\\world")#add \
print("hello\'world")#add '
print("hello\"world")#add "
print("hello\nworld")#line feed
print("hello\rworld")# reverse line feed
print("hello\tworld")# horizontal
print("hello" + "\n" + "world")#same same but diffrent but still same same
MyString = "i love python"
print(MyString[8])
print(MyString[-8])
print(MyString[::1])
print(MyString[0:1:2])# still didn't understand it
print(MyString[::3])
print(len(MyString))
a = "     i love python    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())#shiiiiii

b = "@@@i love python@@@"
print(b.strip("@"))
print(b.rstrip("@"))
print(b.lstrip("@"))#shiiiiii

print(a.title())
print(b.capitalize())

c, d, e = "1", "11", "111"
print(c)
print(d)
print(e)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))

print(a.upper())
print(a.lower())
print(b.split())

e = "ibra"
print(e.center(10,"$"))

print(a.count("o", 0, 9))

print(e.swapcase())
print(e.startswith("i"))
print(e.endswith("r"))
b = "revolution"
print(b.find("i")) #index 7
print(b.find("o",6,15)) #index 8
print(b.rjust(10, "@"))
print(b.ljust(10, "@"))

e = """first line
second line
third line"""
print(e.splitlines())

g = "hello\tworld\ti\tlove\tpython"
print(g.expandtabs(5))

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())

three = " "
four = ""
print(three.isspace())
print(four.isspace())

five = "i love python"
six = " I Love Python"
print(five.islower())
print(six.islower())

seven = "ibra_him"
eight = "ibra--him"

print(seven.isidentifier())
print(eight.isidentifier())

x = "AbbbbAbbbB"
y = "AbbbaaabA1"
print(x.isalpha())
print(y.isalpha())
print(x.isalnum())
print(y.isalnum())

qq = "hello one two one two"
print(qq.replace("one", "1"))


print("-".join(qq))
print(" ".join(qq))
print(",".join(qq))

name = "ibrahim"
age = 19
rank = 1

print("My name is : " + name)
#print("My name is:" + name + "and my age is:" + age) #error
print("my name is:{}".format("ibrahim"))
print("my name is: {} and my age is:{}".format(name,age))
print("my name is : {} and my age is : {} and my rank is : {}".format(name,age,rank))

print("my name is : {:s} and my age is : {:f} and my rank is : {:d}".format(name,age,rank))


mynumberrr = 10
print("my number is : {:d}".format(mynumberrr))
print("my number is : {:f}".format(mynumberrr))
print("my number is : {:.2f}".format(mynumberrr))


mystr = "hello world i don't love python or anyone of you"
print("my message is {}".format(mystr))

print("my message is {:.4s}".format(mystr))
print("my message is {:.21s}".format(mystr))


MyMoney = 100000000
print("my money in bank is : {:d}".format(MyMoney))
print("my money in bank is : {:_d}".format(MyMoney))
print("my money in bank is : {:,d}".format(MyMoney))
#print("my money in bank is : {:&d}".format(MyMoney)) # error



a, b, c = "one", "two", "three"
print("hello {} {} {}".format(a,b,c))
print("hello {2} {0} {1}".format(a,b,c))
print("hello {1} {2} {0}".format(a,b,c))

d,f,g = 10,20,30
print("hello {} {} {}".format(d,f,g))
print("hello {1:d} {2:f} {0:f}".format(d,f,g))

MyName = "ibrahim"
MyAge = 19

print("my name is : {MyName} and my age is : {MyAge}")
print(f"my name is : {MyName} and my age is : {MyAge}")


MyCompnum = 65 + 3j

print(type(MyCompnum))
print("Real part is : {}".format(MyCompnum.real)) # real = 65
print("Imaginary part is : {}".format(MyCompnum.imag)) # imag = 3j


# you can covert from float to int or comp
# you can convert from int to float or comp
# you can't convert from comp to int or float

print(100)
print(float(100))
print(complex(100))

print(10.50)
print(int(10.50))
print(complex(10.50))

print(10+3j)
#print(int(10+3j))
#print(float(10+3j))

# +, -, *, /, %, **, //


print(8 % 2) # 0 
print(13 % 2) # 1


print(2**3)

print( 10 // 2 )
print( 8 // 4 ) 
print( 8 // 3 )

mylist = ["one", "two", 1, 100.5]
print(mylist)
print(mylist[-1])
print(mylist[0])
print(mylist[1:3]) 
print(mylist[:2])



mylist.append("two")
print(mylist)

mylist.append(mynumberrr)
print(mylist)

list = ["one", "two", "three"]

mylist.append(list)
print(mylist)

print(mylist[0])
print(mylist[0][2])
print(mylist[1][2]) # didn't understand

v = "ibrahim"
w = "benaboura"

mylist.extend(v)
print(mylist)

mylist.remove("one")
print(mylist)

n = [100, 2, 34, 24, 0, 14]
n.sort()
print(n)
n.sort(reverse=True)
print(n)

g = ["A", "B", "D", "Z", "F"]
g.sort(reverse=False)
print(g)
g.sort(reverse=True)
print(g)

f = [10 , "D", 12.5]
f.reverse()
print(f)

aa = [1, 2, 3, 4]
#aa.clear()
#print(aa)

bb = aa.copy()
print(aa)
print(bb)

bb.append(5)

print(aa)
print(bb)

cc = [1,2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 2, 1]
print(cc.count(1))

dd = ["zine", "ramy", "ibrahim", "ibrahim", "ramy"]
print(dd.index("ibrahim")) # rank

ee = [1, 2, 3, 4, "A", "B"]
ee.insert(0, "first")
ee.insert(-1, "last")
print(ee)

print(ee.pop(-1))

mytuple1 = ("ibra", "him")
mytuple2 = "ibra", "him"

print(mytuple1)
print(mytuple2)
print(type(mytuple1))
print(type(mytuple2))

print(mytuple1[1])

#mytuple3 = (1, 2, 3, 4)
#mytuple3 [1] = 2
#print(mytuple3)

mytuple4 = ("ibra", "him", "ben", "aboura", 1, 2, 100.3, True)
print(mytuple4[0])

ff = (1, 2, 3, 5)
gg = (4, 6)
hh = ff + gg
print(hh)

mstr = "ibrahim"
mlst = [1, 3]
mtpl = ("A", "C")

print(mstr* 6)
print(mlst* 6)
print(mtpl* 6)

print(mstr.count("i"))
print(mlst.index(3))

nn = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print("the position of index is : {:d}".format(nn.index(7)))
print(f"the position of index is : {nn.index(7)}")

vv = ("A", "B" , 4, "C")


#aaa, bbb, ccc = vv
#print(aaa)
#print(bbb)
#print(ccc)


aaa, bbb, _, ccc = vv
print(aaa)
print(bbb)
print(ccc)

mysetone = {"ibra", "him", 10}
print(mysetone) # no ordered

mysettwo = {"ibra", "ibra", 1, 2, 1}
print(mysettwo) # unique items

#print(mysetone[0:3]) # no slice
myestthree = {"ibra", 100, 100.4, True, (1, 2, 3)}
print(myestthree)

#myestfour= {"ibra", 100, 100.4, True, [1, 2, 3]}
#print(myestfour) # no list or dict in sets

aaaa = {1, 2, 3}
aaaa.clear()
print(aaaa)
bbbb = {2, 3, 4}
print(aaaa | bbbb)
print(aaaa.union(bbbb))
bbbb.add(6)
bbbb.add(7)
print(bbbb)
####
cccc = bbbb.copy()
print(cccc)
bbbb.add(9)
print(bbbb)
print(cccc)

cccc.remove(3)
#cccc.remove(8) # error when you want to remove something doesn't exist in it
print(cccc)

bbbb.discard(7)
bbbb.discard(1) # does not show error when you want to remove something doesn't exist in it
print(bbbb)

k = {"A", 1, 4, True}
print(k.pop()) # random

j = {1, 2, 3}
j.update(k) # random update
print(j)
print("#"* 20)
print(j.difference(k))
print("#"* 20)
j.difference_update(k)
print(j)
print("#"* 20)

nn = {1, 2, 3}
ww = {2, 1, 5}
print(nn.intersection(ww))
print(nn)
 
print("#"* 20)

nn.intersection_update(ww)
print(nn)
print("#"* 20)

print(nn.symmetric_difference(ww))
print(nn)
print("#"* 20)

nn.symmetric_difference_update(ww)
print(nn)

ll = {2, 4, 6, 8}
mm = {2, 4, 6}
hh = {1, 3, 8}
print(ll.issuperset(mm))
print(ll.issuperset(hh))
print("#"* 20) 

print(mm.issubset(ll))
print(mm.issubset(hh))

print("#"* 20)
print(ll.isdisjoint(mm))
print(ll.isdisjoint(hh))
print(mm.isdisjoint(hh))











