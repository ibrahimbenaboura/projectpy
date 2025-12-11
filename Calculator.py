
print("=== Simple Calculator ===")


def add(a, b) :
    return a + b
def sub(a, b) :
    return a - b 
def mul(a, b) :
    return a * b
def div(a, b) :
    return a / b

a = int(input("Write the value of the first number :"))
b = int(input("Write the vlaue of the second number :"))
while True :
    print("Choose the parametre :")
    print("1- Add")
    print("2- Sub")
    print("3- Mul")
    print("4- Div")

    choice = float(input("Your choice is :"))

    if choice == 1 :
        print(add(a, b))
        break
    elif choice == 2 :
        print(sub(a, b))
        break
    elif choice == 3 :
        print(mul(a, b))
        break
    elif choice == 4 :
        print(div(a, b))
        break
    else :
        print("You have wrong input")
        break



















