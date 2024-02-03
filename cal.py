def add(a,b):
    add=a+b
    print("Result:",add)

def sub(a,b):
    sub=a-b
    print("Result:",sub)

def mul(a,b):
    mul=a*b
    print("Result:",mul)

def div(a,b):
    div=a/b
    print("Result:",div)

def mod(a,b):
    mod=a%b
    print("Result:",mod)


def calcultor():
    print("Welcome to my calcultor Program")
    print("**********************************")
    num1 = float(input("First value:"))
    num2 = float(input("Second value:"))
    
    print("*************************************")
    print("Task Name")
    print("For Adding number :1")
    print("For Substraction number:2")
    print("For multiplition number:3")
    print("For dividation number:4")
    print("For Modulas number:5")

    chooseTask = int(input("Please choose your Task:"))
    print("*****************************************")

    if(chooseTask==1):
        add(num1,num2)
    
    elif(chooseTask==2):
        sub(num1,num2)
    
    elif(chooseTask==3):
        mul(num1,num2)
    
    elif(chooseTask==4):
        div(num1,num2)
    
    elif(chooseTask==5):
        mod(num1,num2)
    
    else:
        print("Invaild selected task")


calcultor()