def add(a, b):
    answer = a + b
    print(str(a),"+", str(b),"=", str(answer) + "/n")

def sub(a, b):
    answer = a - b
    print(str(a),"-", str(b),"=", str(answer) + "/n")

def mul(a, b):
    answer = a * b
    print(str(a),"*", str(b),"=", str(answer) + "/n")

def div(a, b):
    answer = a / b
    print(str(a),"/", str(b),"=", str(answer) + "/n")  


while True:
    print("A for +")
    print("B for -") 
    print("C for *") 
    print("D for /") 
    print("Q to quit")
    choice = input("input your choice: ").upper()

    if choice == "A":
        print("Addition")
        a = int(input("inpute the first number: ").isdigit)
        b = int(input("input the second number: ").isdigit)
        add(a, b)
        break
    elif choice == "B":
        print("Subtraction")
        a = int(input("inpute the first number: "))
        b = int(input("input the second number: "))
        sub(a, b)
        break
    elif choice == "C":
        print("Multiply")
        a = int(input("inpute the first number: "))
        b = int(input("input the second number: "))
        mul(a, b)
        break
    elif choice == "D":
        print("Division")
        a = int(input("inpute the first number: "))
        b = int(input("input the second number: "))
        div(a, b)
        break
    elif choice == "Q":
        print("Basic Calculator quited.")
        quit()
    else:
        print("invalid selection please choose A,B,C,D or Q: ")
        continue